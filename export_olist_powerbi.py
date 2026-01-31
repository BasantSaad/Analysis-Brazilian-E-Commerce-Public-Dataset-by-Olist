
# export_olist_powerbi_safe.py
# Optimized for low memory & Power BI compatibility

import pandas as pd
import numpy as np
import os, gc

DATA_PATH = r"D:\About ME\Digital hub_data analysis\Olist E-Commerce"
OUT_PATH = os.path.join(os.path.dirname(__file__), "powerbi_out")
os.makedirs(OUT_PATH, exist_ok=True)

# -------------------- LOAD (LIGHT) --------------------
orders = pd.read_csv(
    os.path.join(DATA_PATH, "olist_orders_dataset.csv"),
    usecols=[
        "order_id","customer_id","order_status",
        "order_purchase_timestamp",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ],
    parse_dates=[
        "order_purchase_timestamp",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
)

order_items = pd.read_csv(
    os.path.join(DATA_PATH, "olist_order_items_dataset.csv"),
    usecols=["order_id","product_id","price","freight_value"]
)

payments = pd.read_csv(
    os.path.join(DATA_PATH, "olist_order_payments_dataset.csv"),
    usecols=["order_id","payment_value","payment_type"]
)

reviews = pd.read_csv(
    os.path.join(DATA_PATH, "olist_order_reviews_dataset.csv"),
    usecols=["order_id","review_score"]
)

# dtype optimization
order_items["price"] = order_items["price"].astype("float32")
order_items["freight_value"] = order_items["freight_value"].astype("float32")

# -------------------- FACT ORDERS --------------------
order_agg = order_items.groupby("order_id").agg(
    total_price=("price","sum"),
    total_freight=("freight_value","sum"),
    num_items=("product_id","count")
).reset_index()

payment_agg = payments.groupby("order_id").agg(
    payment_value=("payment_value","sum"),
    payment_type=("payment_type","first")
).reset_index()

review_agg = reviews.groupby("order_id")["review_score"].mean().reset_index()

fact = orders.merge(order_agg, on="order_id", how="left") \
             .merge(payment_agg, on="order_id", how="left") \
             .merge(review_agg, on="order_id", how="left")

fact["delivery_days"] = (
    fact["order_delivered_customer_date"] - fact["order_purchase_timestamp"]
).dt.days

fact["delivery_delay"] = (
    fact["order_delivered_customer_date"] - fact["order_estimated_delivery_date"]
).dt.days

fact["is_late"] = (fact["delivery_delay"] > 0).astype("int8")
fact["date_key"] = fact["order_purchase_timestamp"].dt.strftime("%Y%m%d").astype(int)

fact = fact[fact["order_status"] == "delivered"]

fact.to_csv(os.path.join(OUT_PATH, "fact_orders.csv"), index=False)

# free memory
del order_items, payments, reviews, orders
gc.collect()

# -------------------- PRODUCT PERFORMANCE --------------------
products = pd.read_csv(
    os.path.join(DATA_PATH, "olist_products_dataset.csv"),
    usecols=["product_id","product_category_name"]
)

review_per_order = review_agg.set_index("order_id")["review_score"]

product_perf = (
    pd.read_csv(
        os.path.join(DATA_PATH, "olist_order_items_dataset.csv"),
        usecols=["order_id","product_id","price","freight_value"]
    )
    .join(review_per_order, on="order_id")
    .groupby("product_id")
    .agg(
        order_count=("order_id","count"),
        total_revenue=("price","sum"),
        avg_price=("price","mean"),
        avg_freight=("freight_value","mean"),
        avg_rating=("review_score","mean")
    )
    .reset_index()
    .merge(products, on="product_id", how="left")
)

product_perf.to_csv(os.path.join(OUT_PATH, "analysis_product_performance.csv"), index=False)

# -------------------- CATEGORY SUMMARY --------------------
category_summary = product_perf.groupby("product_category_name").agg(
    product_count=("product_id","count"),
    order_count=("order_count","sum"),
    total_revenue=("total_revenue","sum"),
    avg_price=("avg_price","mean"),
    avg_rating=("avg_rating","mean")
).reset_index().sort_values("total_revenue", ascending=False)

category_summary.to_csv(os.path.join(OUT_PATH, "analysis_category_summary.csv"), index=False)

# -------------------- MONTHLY TRENDS --------------------
monthly = fact.groupby(
    fact["order_purchase_timestamp"].dt.to_period("M")
).agg(
    order_count=("order_id","count"),
    revenue=("total_price","sum"),
    avg_rating=("review_score","mean"),
    avg_delivery_days=("delivery_days","mean"),
    late_rate=("is_late","mean")
).reset_index()

monthly["year_month"] = monthly["order_purchase_timestamp"].astype(str)
monthly.drop(columns=["order_purchase_timestamp"], inplace=True)

monthly.to_csv(os.path.join(OUT_PATH, "analysis_monthly_trends.csv"), index=False)

# -------------------- KPI SUMMARY --------------------
kpi = pd.DataFrame({
    "KPI":[
        "Total Orders","Total Revenue","Avg Order Value",
        "Avg Rating","On-Time Delivery %"
    ],
    "Value":[
        len(fact),
        fact["total_price"].sum(),
        fact["total_price"].mean(),
        fact["review_score"].mean(),
        (1 - fact["is_late"].mean())*100
    ]
})

kpi.to_csv(os.path.join(OUT_PATH, "kpi_summary.csv"), index=False)

print("DONE - Files created in powerbi_out folder")
