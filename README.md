# DMart Lead Time & Inventory Holding Cost Analysis

This project analyzes DMart sample sales data to understand how **lead time** — the time between placing an order and receiving it — affects average inventory holding costs.

By simulating different lead times and calculating their impact, this analysis shows how faster delivery cycles can help retailers run leaner, reduce locked-up capital, and improve cash flow.

---

## Project Overview

- **Data:** DMart sample sales data (`DMart_sales.csv`)
- **Goal:** Show how varying lead times change average inventory holding costs
- **Key Metric:** `Holding Cost = Total × Daily Holding Rate × Lead Time`
- **Tools:**
  - **Python** (`pandas`, `numpy`) — data cleaning, lead time simulation, cost calculation
  - **Tableau Public** — interactive dashboard to visualize the trend

---

## Files Included

- **`DMart_sales.csv`** — Raw DMart sales data (Unit Price, Quantity, Total)
- **`Add_lead_time.py`** — Python script to add a `Lead_Time` column (randomly 1–7 days)
- **`DMart_sales_with_lead_time.csv`** — Output with simulated lead time
- **`DMart_analysis.py`** — Python script to:
  - Load sales data
  - Add lead time
  - Calculate holding cost (`Holding Cost = Total × Daily Rate × Lead Time`)
  - Create a pivot showing how average holding cost changes with lead time
  - Visualize results with a bar chart

---

## Key Insight

**Longer lead times → Higher average holding costs → More working capital tied up.**  
**Shorter lead times → Leaner operations → Better cash flow.**

---

## Tools Used

- **Python** (`pandas`, `numpy`, `matplotlib`) — Data cleaning, lead time simulation, cost calculation, visualization
- **Tableau Public** — Interactive dashboard to share and present the trend

---

## Project Goal

- **Data:** DMart sample sales data (`DMart_sales.csv`)
- **Goal:** Show how varying lead times affect average inventory holding costs
- **Key Metric:** 'Holding Cost = Total × Daily Holding Rate × Lead Time'

---

## How To Run

1. Clone this repo.
2. Create a virtual environment & install dependencies:
   ```bash
   pip install pandas numpy matplotlib
3. Run Add_lead_time.py to add the Lead_Time column and save a new CSV.
4. Run DMart_analysis.py to calculate, group, and plot the trend.
5. See the interactive dashboard: Tableau Public Dashboard
   [https://public.tableau.com/app/profile/mounisha.u/viz/DMart_LeadTime_HoldingCost/DMartImpactofLeadTimeonInventoryHoldingCost]

---

## Outcome

This project shows practical data wrangling and visualization skills using realistic retail data.  
It connects supply chain lead time with a key business metric: inventory holding cost — valuable for retailers and supply chain analysts.

---

**Author:** Mounisha Udatha  
**Connect:** [LinkedIn](https://www.linkedin.com/in/mounisha-udatha/) | [GitHub](https://github.com/MounishaU)

