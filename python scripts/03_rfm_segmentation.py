import pandas as pd
import numpy as np

df = pd.read_csv("data/sales_transactions.csv")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Setting Reference date using last transaction date in dataset
reference_date = df['InvoiceDate'].max()

# Calculating RFM Metrics [Recency, Frequency, Monetary]
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalAmount': 'sum'
}).reset_index()

# Renaming Columns for better understanding
rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

# Recency Score
def recency_score(x):
    if x <= 30:
        return 3
    elif x <= 90:
        return 2
    else:
        return 1

# Frequency Score
def frequency_score(x):
    if x >= 10:
        return 3
    elif x >= 5:
        return 2
    else:
        return 1

# Monetary Score
def monetary_score(x):
    if x >= 5000:
        return 3
    elif x >= 2000:
        return 2
    else:
        return 1

rfm['R_Score'] = rfm['Recency'].apply(recency_score)
rfm['F_Score'] = rfm['Frequency'].apply(frequency_score)
rfm['M_Score'] = rfm['Monetary'].apply(monetary_score)


# Customer Segmentation using RFM Scores
def segment_customer(row):
    if row['R_Score'] == 3 and row['F_Score'] == 3:
        return 'Best Customers'
    elif row['R_Score'] >= 2 and row['F_Score'] >= 2:
        return 'Good Customers'
    elif row['R_Score'] == 1:
        return 'Inactive Customers'
    else:
        return 'Low Value Customers'

rfm['Segment'] = rfm.apply(segment_customer, axis=1)

rfm.to_csv("data/customer_rfm.csv", index=False)

print("RFM Segmentation Success")
