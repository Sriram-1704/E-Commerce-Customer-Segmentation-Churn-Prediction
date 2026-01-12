import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/sales_transactions.csv")

# Monthly Sales
df['Month'] = pd.to_datetime(df['InvoiceDate']).dt.to_period('M')

monthly_sales = df.groupby('Month')['TotalAmount'].sum()

plt.figure(figsize=(15,10))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.savefig("images/monthly_sales.png")
plt.close()

# Top 10 Country-wise Sales
country_sales = df.groupby('Country')['TotalAmount'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(15,12))
country_sales.plot(kind='bar')
plt.title("Top 10 Countries by Sales")
plt.savefig("images/country_sales.png")
plt.close()

