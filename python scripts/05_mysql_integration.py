import pandas as pd
import mysql.connector

df = pd.read_csv("data/customer_churn.csv")

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",   
    database="ecommerce_project"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO customer_churn
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
conn.close()

print(" Data inserted into MySQL")
