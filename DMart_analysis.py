import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load
df = pd.read_csv("dmart_sales.csv")
print(df.head())

# Add Lead Time (1-7 days)
np.random.seed(42)
df['Lead_Time_Days'] = np.random.randint(1, 8, size=len(df))

# Calculate Holding Cost
daily_rate = 0.005
df['Holding_Cost'] = df['Total'] * daily_rate * df['Lead_Time_Days']

# Pivot
pivot = df.groupby('Lead_Time_Days')['Holding_Cost'].mean().reset_index()
print(pivot)

# Plot
plt.figure(figsize=(8, 5))
plt.bar(pivot['Lead_Time_Days'], pivot['Holding_Cost'], color='skyblue')
plt.xlabel('Lead Time (Days)')
plt.ylabel('Average Holding Cost')
plt.title('Impact of Lead Time on Inventory Holding Cost')
plt.xticks(pivot['Lead_Time_Days'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
