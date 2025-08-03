# 📊 DMart Lead Time & Inventory Holding Cost Analysis

---

## 🔍 Problem

Retail chains like DMart risk higher working capital costs if supply chain lead times increase.  
Longer lead times → higher inventory → more tied-up cash.

---

## 🛠️ Solution

Analyzed 100,000+ rows of sales data to simulate how lead time changes affect inventory holding costs.  
Built a Python model ('pandas', 'NumPy') to calculate daily holding costs and compare scenarios.

---

## 💡 Key Findings

Extending lead time from 1 to 7 days can increase holding costs by **600%**.  
DMart can use this insight to negotiate faster deliveries or improve internal logistics to cut costs.

---

## 📈 Deliverables

- 📂 **Python scripts** — EDA, simulation, cost model
- 📊 **Tableau Dashboard** — Interactive visualization for decision makers

👉 [View Tableau Dashboard](https://public.tableau.com/app/profile/mounisha.u/viz/DMart_LeadTime_HoldingCost/DMartImpactofLeadTimeonInventoryHoldingCost)

---

## ✅ Skills Demonstrated

- Python EDA & scenario modeling
- Tableau dashboard design for non-technical audiences
- Clear documentation for business stakeholders

---

## 📌 Takeaway

This project shows how supply chain data can directly support cost-saving decisions and supplier negotiations.

---

# 📂 Full Project Details


## Project Overview

- **Data:** DMart sample sales data (`DMart_sales.csv`)
- **Goal:** Show how varying lead times change average inventory holding costs
- **Key Metric:** `Holding Cost = Total × Daily Holding Rate × Lead Time`
- **Tools:**
  - **Python** ('pandas', 'numpy') — data cleaning, lead time simulation, cost calculation
  - **Tableau Public** — interactive dashboard to visualize trends

---

## Files Included

- **`DMart_sales.csv`** — Raw DMart sales data (Unit Price, Quantity, Total)
- **`Add_lead_time.py`** — Python script to add a `Lead_Time` column (random values 1–7 days)
- **`DMart_sales_with_lead_time.csv`** — Output dataset with simulated lead time
- **`DMart_analysis.py`** — Python script to:
  - Load sales data
  - Add lead time
  - Calculate holding cost (`Holding Cost = Total × Daily Rate × Lead Time`)
  - Generate a pivot table showing how average holding cost changes with lead time
  - Visualize results with a bar chart

---

## Key Insight

**Longer lead times → Higher average holding costs → More working capital tied up.**  
**Shorter lead times → Leaner operations → Better cash flow.**

---

## Tools Used

- **Python** (`pandas`, `numpy`, `matplotlib`) — Data cleaning, simulation, cost modeling, visualization
- **Tableau Public** — Dashboard for communicating results clearly

---

## How To Run

1. Clone this repo.
2. Create a virtual environment & install dependencies:
   ```bash
   pip install pandas numpy matplotlib
Run Add_lead_time.py to add the Lead_Time column and save a new CSV.

Run DMart_analysis.py to calculate, group, and plot the trend.

View the interactive dashboard on [Tableau]
[https://public.tableau.com/app/profile/mounisha.u/viz/DMart_LeadTime_HoldingCost/DMartImpactofLeadTimeonInventoryHoldingCost]

## Screenshot 

<img width="476" height="490" alt="dashboard_screenshot" src="https://github.com/user-attachments/assets/32311da0-5cc5-4d5e-8d54-b0334f909691" />

---

## Outcome

This project shows practical data wrangling and visualization skills using realistic retail data.  
It demonstrates how supply chain lead time directly drives inventory costs - insights any retail analyst or procurement team can act on.

---

**Author:** Mounisha Udatha  
**Connect:** [LinkedIn](https://www.linkedin.com/in/mounisha-udatha/) | [GitHub](https://github.com/MounishaU)

