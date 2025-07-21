import pandas as pd
import numpy as np

# Load your original DMart sales CSV
df = pd.read_csv('DMart_sales.csv')

# Add a Lead_Time column with random integers from 1 to 7
df['Lead_Time'] = np.random.randint(1, 8, size=len(df))

# Save to a new CSV
df.to_csv('DMart_sales_with_lead_time.csv', index=False)

print("✅ Lead_Time column added. New file: DMart_sales_with_lead_time.csv")
