# 🛒 Olist E-Commerce: Data Exploration Analytics

Brazilian Marketplace Analytics & Insights

---

## 📋 Overview

This Jupyter notebook provides comprehensive data exploration and analysis of the Olist E-Commerce dataset, a Brazilian marketplace dataset containing information about orders, customers, products, sellers, and reviews from 2016-2018.

## 🎯 Objectives

1. **Load all 8 datasets** - Import and validate all data sources
2. **Understand table relationships** - Map connections between datasets
3. **Check data quality** - Identify and handle missing values and errors
4. **Initial exploratory analysis** - Generate insights through visualizations
5. **Validate data model** - Verify data integrity and relationships

---

## 📊 Dataset Overview

The analysis includes **8 interconnected datasets**:

| Dataset | Description | Records |
|---------|-------------|---------|
| **Customers** | Customer information and location | 99,441 rows |
| **Orders** | Order details and status | 99,441 rows |
| **Order Items** | Individual items within orders | 112,650 rows |
| **Products** | Product catalog and categories | 32,951 rows |
| **Payments** | Payment transactions | 103,886 rows |
| **Reviews** | Customer reviews and ratings | 99,224 rows |
| **Sellers** | Seller information and location | 3,095 rows |
| **Geolocation** | Zip code coordinate data | 1,000,163 rows |

---

## 🔍 Key Analysis Components

### 1. Data Loading
- Automated loading of all 8 CSV files
- Shape validation and error checking
- Dataset structure inspection

### 2. Individual Table Exploration
- First rows preview for each dataset
- Data type analysis
- Missing value detection and documentation

### 3. Data Quality Assessment
- **Missing Values Analysis**: Systematic identification of null/missing data
- **Data Error Detection**: Found and documented 10 data errors
- **Philosophy**: "Missing doesn't mean wrong" - Context-aware data handling
- Strategic decisions on missing value treatment

### 4. Relationship Validation
- Primary and foreign key validation
- Cross-table relationship verification
- Data model integrity checks

### 5. Initial Visualizations
- Statistical summaries
- Distribution analysis
- Key metric visualizations

---

## 🛠️ Technologies Used

- **Python 3.x**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **seaborn** - Statistical visualizations
- **datetime** - Date/time handling

---

## 📁 File Structure

```
.
├── 01_data_exploration.ipynb          # Main analysis notebook
├── README.md                          # This file
└── data/                             # Data directory (not included)
    ├── olist_customers_dataset.csv
    ├── olist_orders_dataset.csv
    ├── olist_order_items_dataset.csv
    ├── olist_products_dataset.csv
    ├── olist_order_payments_dataset.csv
    ├── olist_order_reviews_dataset.csv
    ├── olist_sellers_dataset.csv
    └── olist_geolocation_dataset.csv
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Running the Notebook

1. **Clone or download** this repository
2. **Download the Olist dataset** from [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce)
3. **Update the data path** in the notebook:
   ```python
   data_path = r"YOUR_PATH_HERE"
   ```
4. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook 01_data_exploration.ipynb
   ```
5. **Run all cells** to execute the analysis

---

## 🔑 Key Findings

### Data Quality Insights
- ✅ Successfully loaded all 8 datasets
- 🔍 Identified missing values across multiple tables
- 🐛 Detected and documented 10 data errors
- 📊 Validated relationships between all tables

### Missing Data Strategy
The analysis implements a thoughtful approach to missing values:
- Context-aware assessment of each missing field
- Documentation of why certain fields may be legitimately null
- Strategic decisions on imputation vs. retention
- Preservation of data integrity

---

## 📈 Analysis Highlights

- 🔗 **Data Loading**: Systematic approach using `os.path.join()` for cross-platform compatibility
- 🎨 **Visualization Setup**: Pre-configured seaborn styling with `whitegrid` theme
- 📏 **Figure Sizing**: Default 14x6 inch plots for readability
- ⚠️ **Error Handling**: Comprehensive try-except blocks for robust data loading

---

## 📝 Notes

- The notebook uses a **Windows file path** format - update the `data_path` variable for your system
- **Warnings are suppressed** for cleaner output - remove `warnings.filterwarnings('ignore')` for debugging
- The analysis assumes all 8 CSV files are in the same directory

---

## 🤝 Contributing

This is an exploratory analysis notebook. Feel free to:
- Extend the analysis with additional visualizations
- Add statistical tests
- Incorporate machine learning models
- Enhance data quality checks

---

## 📄 License

This project analyzes the Olist public dataset. Please refer to the [original dataset license](https://www.kaggle.com/olistbr/brazilian-ecommerce) for usage terms.

---

## 👤 Author

Data analysis and exploration of Brazilian e-commerce marketplace data.

---

## 🙏 Acknowledgments

- **Olist** for providing the public dataset
- **Kaggle** for hosting the data
- Brazilian E-Commerce community for insights and context

---

## 📚 Next Steps

After completing this exploratory analysis, consider:
1. **Feature Engineering** - Create new variables for modeling
2. **Time Series Analysis** - Analyze trends over time
3. **Customer Segmentation** - Cluster analysis of customer behavior
4. **Predictive Modeling** - Build models for sales forecasting or churn prediction
5. **Geospatial Analysis** - Deep dive into location-based patterns

---

**Happy Analyzing! 📊🚀**
