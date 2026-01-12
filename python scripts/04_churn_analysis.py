import pandas as pd
import matplotlib.pyplot as plt

rfm = pd.read_csv("data/customer_rfm.csv")

# Logic for Churn
rfm['Churn'] = rfm['Recency'].apply(
    lambda x: 1 if x > 90 else 0
)

# Save churn data
rfm.to_csv("data/customer_churn.csv", index=False)

churn_counts = rfm['Churn'].value_counts()

plt.bar(churn_counts.index, churn_counts.values)
plt.xticks([0, 1], ['Active', 'Churned'])
plt.title("Customer Churn Distribution")
plt.xlabel("Customer Status")
plt.ylabel("Number of Customers")

plt.savefig("images/churn_distribution.png")
plt.show()

print(" Churn analysis completed ")
