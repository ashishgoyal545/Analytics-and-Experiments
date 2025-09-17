# 📊 Analytics & Experiments

Utilities and templates for **funnels, churn, and A/B tests**.  
These are **PM-friendly tools** to reason about metrics, experiment design, and decision-making.  

---

## 📂 Contents
- 🧮 **[ab_test_calculator.py](./ab_test_calculator.py)** → Sample size & significance calculator (CLI).  
- 📈 **[analyze_funnel.ipynb](./analyze_funnel.ipynb)** → Funnel analysis notebook with quick visualizations.  
- 🗂 **[funnel_example.csv](./funnel_example.csv)** → Mock funnel dataset for demos.  

---

## 📊 Example Funnel (mock data)

| Step             | Users | Drop-off |
|------------------|-------|----------|
| Landing Page     | 1,000 | -        |
| Signup Started   |   600 | 40%      |
| Signup Completed |   400 | 33%      |
| Activated        |   250 | 38%      |

➡ Funnel conversion = **25%** (Landing → Activated).  

---

## 🧪 A/B Test Calculator (CLI)
```bash
python ab_test_calculator.py --p1 0.1 --p2 0.12 --alpha 0.05 --power 0.8
