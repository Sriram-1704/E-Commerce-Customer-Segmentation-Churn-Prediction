🛒 E-Commerce Customer Segmentation & Churn Prediction Dashboard
📌 Project Overview

This project focuses on analyzing customer behavior, segmenting customers using RFM analysis, and identifying churn patterns in an e-commerce business.
The goal is to help businesses reduce churn, improve retention, and identify high-risk customer segments using Python, SQL, and Power BI.

The project follows a complete data analytics lifecycle:

Data Cleaning & Processing

Exploratory Data Analysis (EDA)

Customer Segmentation (RFM)

Churn Analysis

Interactive Dashboards in Power BI

🧠 Business Objectives

Identify churned vs retained customers

Segment customers based on Recency, Frequency, and Monetary value

Detect high-risk customer segments

Provide actionable insights for retention strategies

🛠️ Tech Stack

Python (Pandas, NumPy, Matplotlib)

SQL (MySQL)

Power BI

📂 Project Structure

Ecommerce-Customer-Segmentation-Churn-Prediction/

│

├── data/

│   ├── raw_data.csv

│   ├── customer_churn.csv

│   ├── customer_rfm.csv

│   └── sales_transactions.csv
│

├── python_scripts/

│   ├── 01_Data_Cleaning.py

│   ├── 02_EDA.py

│   ├── 03_rfm_segmentation.py

│   ├── 04_churn_analysis.py

│   └── 05_mysql_integration.py

│

├── sql/

│   ├── simple_queries.sql

│   └── analysis_queries.sql

│

├── powerbi/

│   └── Ecommerce_Customer_Segmentation_Churn_Prediction.pbix

│


├── reports/

│   ├── Executive_Overview_Dashboard.png

│   ├── Churn_Analysis_Dashboard.png

│   ├── Churn_Risk_Insights_Dashboard.png

│   ├── Ecommerce_Customer_Segmentation_Churn_Prediction_Dashboard.pdf

│   └── Insights_Summary.md

│

├── images/

│   ├── churn_distribution.png

│   ├── monthly_sales.png

│   └── country_sales.png

│

├── requirements.txt

└── README.md

📊 Power BI Dashboards
🔹 Executive Overview Dashboard

Key Insights:

Total customers and overall churn rate

Sales performance overview

Customer segmentation summary

High-level KPIs for decision-makers

🔹 Churn Analysis Dashboard

Key Insights:

Retained vs churned customers comparison

Churn distribution by customer segments

Identification of churn-heavy segments

🔹 Churn Risk Insights Dashboard

Key Insights:

Churn rate (%) by customer segment

Average recency (days since last purchase)

Average purchase frequency patterns

Early warning signals for high-risk customers

📈 Key Metrics & Measures

Total Customers

Churned Customers

Retained Customers

Churn Rate (%)

RFM Scores (Recency, Frequency, Monetary)

Average Purchase Frequency

Average Recency (Days)

🧪 Data Processing Workflow

1️⃣ Data Cleaning

Removed duplicates and null values

Standardized column names

Converted data types for analysis

2️⃣ Exploratory Data Analysis (EDA)

Sales trends analysis

Customer distribution analysis

Churn distribution visualization

3️⃣ RFM Segmentation

Calculated R, F, M scores

Created customer segments:

Best Customers

Good Customers

Low Value Customers

Inactive Customers

4️⃣ Churn Analysis

Identified churned customers

Compared churn across segments

Calculated churn rates

5️⃣ Visualization & Reporting

Built interactive dashboards in Power BI

Designed clean UI with consistent color themes

Exported dashboard images for documentation

📝 Insights Summary

Detailed business insights and recommendations are documented here:
📄 reports/Insights_Summary.md

🚀 How to Run This Project

🔹 Python

pip install -r requirements.txt

python python_scripts/01_Data_Cleaning.py

🔹 Power BI

Open .pbix file from powerbi/ folder

Refresh data sources if required

🎯 Key Takeaways

Inactive customers contribute the highest churn

High-value customers have low churn risk

Recency is a strong indicator of churn behavior

Targeted retention strategies can significantly reduce churn

👤 Author

Sri Ram

MCA Graduate | Aspiring Data Analyst / BI Developer

Skills: Python | SQL | Power BI | Data Analysis | Visualization
