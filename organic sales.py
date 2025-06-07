# sales_analysis.py
# 🔍 Organic India Sales Analysis using Python (Pandas, Matplotlib, Seaborn)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel data
xls = pd.ExcelFile("Main All Data.xlsx")

# Parse sheets
sales = xls.parse("Sales")
products = xls.parse("Product")
customers = xls.parse("Customer")

# Merge Sales with Product info
sales = sales.merge(products, how="left", left_on="Product Code", right_on="Product Code")

# Merge Sales with Customer info
sales = sales.merge(customers, how="left", left_on="Customer ID", right_on="Customer ID")

# Convert date
sales['Date'] = pd.to_datetime(sales['Date'])

# Calculate Revenue
sales['Revenue'] = sales['Vol'] * (sales['Price/kg'] / 1000)

# Summary metrics
total_revenue = sales['Revenue'].sum()
total_bills = sales['Bill No.'].nunique()
total_customers = sales['Customer ID'].nunique()

print(f"Total Revenue: ₹{total_revenue/1e6:.2f}M")
print(f"Total Bills Generated: {total_bills}")
print(f"Total Customers: {total_customers}")

# Revenue by Region
revenue_by_region = sales.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
print("\nRevenue by Region:")
print(revenue_by_region)

# Customer Type Contribution
customer_type_pct = sales['Customer Type'].value_counts(normalize=True) * 100
print("\nCustomer Type Contribution (%):")
print(customer_type_pct.round(2))

# Top Product Categories
top_categories = sales.groupby('Parent Category')['Revenue'].sum().sort_values(ascending=False)
print("\nTop Product Categories by Revenue:")
print(top_categories)

# OPTIONAL: Visualization (Uncomment to display)

# sns.set(style="whitegrid")
# plt.figure(figsize=(10, 6))
# sns.barplot(x=revenue_by_region.index, y=revenue_by_region.values)
# plt.title("Revenue by Region")
# plt.ylabel("Revenue (INR)")
# plt.xlabel("Region")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
