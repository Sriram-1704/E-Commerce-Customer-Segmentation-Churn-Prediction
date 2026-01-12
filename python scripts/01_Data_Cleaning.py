import pandas as pd
df = pd.read_csv("data/raw_data.csv", encoding="latin1")

print("Rows and Columns:", df.shape)

# Removing Missing CustomerIDs
df = df.dropna(subset=['CustomerID'])

# Removing Cancelled Invoices
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Removing Negative or Zero Quantity
df = df[df['Quantity'] > 0]

# Removing Zero or Negative Price
df = df[df['UnitPrice'] > 0]

# Converting InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors="coerce")

# Converting CustomerID to Integer
df['CustomerID'] = df['CustomerID'].astype(int)

# Creating New Column for Total Amount 
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Saving Cleaned Data
df.to_csv("data/sales_transactions.csv", index=False)

print("Data cleaning completed successfully.")
