# Brazilian E-Commerce (Olist) Analytics Project 🛒

## 📋 Project Overview

Analyze **100,000+ real orders** from Brazilian e-commerce platform Olist (2016-2018)
- **8 interconnected tables** with complete customer journey data
- **Real business relationships** via customer_id, order_id, product_id
- **Rich analysis** possibilities: CLV, segmentation, operations, recommendations

**Business Goal:** Optimize customer value, operations, and profitability through data-driven insights.

---

## 📊 Dataset Structure - **8 Connected Tables**

```
customers (99,441) → orders (99,441) → order_items (112,650) → products (32,951)
                          ↓                    ↓
                      payments              sellers (3,095)
                          ↓
                       reviews
```

**Download:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## 🎯 Key Business Questions

1. What makes a high-value customer? (CLV calculation)
2. Which product categories drive profitability?
3. How does delivery performance affect ratings?
4. Can we predict customer churn?
5. How to build product recommendations?

---

## 🗂️ Project Structure

```
olist-ecommerce/
├── data/raw/           # 8 CSV files from Kaggle
├── data/processed/     # Cleaned & merged data
├── data/powerbi/       # Star schema for Power BI
├── notebooks/          # 8 analysis notebooks
├── scripts/            # Python utilities
└── docs/               # Documentation
```

---

## 🚀 Quick Start

```bash
# 1. Download data from Kaggle
# 2. Run setup
python setup_project.py

# 3. Execute notebooks in order
jupyter notebook notebooks/01_data_exploration.ipynb
```

---

## 📈 Expected Key Insights

- **Customer Retention:** Low repeat rate (1.03 avg purchases) = big opportunity
- **Delivery Impact:** Every day late = -0.05 rating points
- **Revenue Concentration:** Top 20% customers = 60-80% revenue
- **Product Winners:** Health & Beauty, Watches highest margin
- **Payment Behavior:** Installments increase order value 40%

---

**Full documentation in files provided!**
