# 🚦 Big Data Final Project – Predicting Injury Severity in Chicago Traffic Crashes

## 👥 Group Members
- Asif Imtiaz  
- Muhammad Hammaz  
- Andrey Martynenko  
- Martin Zuluaga

---

## 🎯 Objective

To predict the **most severe injury outcome** of a traffic crash using machine learning and over 2 million crash records from the **City of Chicago** open data portal. This project aims to support **faster emergency response**, **resource allocation**, and **urban planning** through **data-driven modeling**.

---

## 🗂️ Data Sources

- [Traffic Crashes – Crashes](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if)
- [Traffic Crashes – People](https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d)
- [Traffic Crashes – Vehicles](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3)

These datasets were **joined using CRASH_RECORD_ID and VEHICLE_ID**, forming a master dataset of 2.3M rows and 143 features.

---

## 🔍 Phase-wise Breakdown

### ✅ Phase 1–3: Loading and EDA
- Cleaned and joined 3 datasets.
- Handled nulls and selected relevant features.
- Observed **class imbalance** in injury severity.

### ✅ Phase 4–5: Modeling Direction
- Target Variable: `MOST_SEVERE_INJURY`
- Decided on **multi-class classification**.
- Created a simplified 3-class injury setup:
  - No Injury
  - Minor Injury
  - Severe Injury (includes Fatal + Incapacitating)

### ✅ Phase 6: Feature Engineering
- Selected 11 features (7 categorical + 4 numerical).
- Applied `StringIndexer`, `OneHotEncoder`, `VectorAssembler`.
- Split data into training (80%) and testing (20%).

### ✅ Phase 7–10: Modeling & Evaluation

| Model                | Accuracy | F1 Score |
|---------------------|----------|----------|
| Logistic Regression | ~84%     | ~79%     |
| Decision Tree       | ~81%     | ~75%     |
| Random Forest       | ~87%     | ~82%     |
| GBTClassifier       | ~89%     | ~83%     |

- Evaluation Metrics:
  - Accuracy, F1 Score, Precision, Recall
  - Confusion Matrix Visualizations
- Feature Importance Visuals included

### ✅ Phase 11: SparkSQL Analysis
Included 8+ SQL queries (e.g., weather breakdown, lighting conditions, injury types, etc.) with interpretations.

---

## 📈 Key Findings

- **83%** of crashes resulted in no injuries.
- Features like `CRASH_HOUR`, `WEATHER_CONDITION`, `LIGHTING_CONDITION`, and `ROADWAY_SURFACE_COND` were highly predictive.
- **Random Forest** showed the best balance between performance and interpretability.

---

## 📌 Final Recommendations

Based on model results and exploratory insights, we recommend the City of Chicago:

1. **Integrate our model into 911 systems**  
   Flag potentially severe crashes in real-time based on crash conditions to help **dispatchers prioritize emergency responses**.

2. **Deploy Predictive Heatmaps**  
   Use daily-updated injury prediction maps to **optimize EMS, police, and signage deployment** in high-risk zones.

3. **Enhance Public Alerts**  
   Trigger **weather-based alerts** and targeted speed enforcement during rain, snow, or low-light conditions.

4. **Upgrade Infrastructure**  
   Prioritize lighting, barriers, and road maintenance at historically dangerous intersections or road segments.

5. **Monitor and Retrain Quarterly**  
   Continuously **retrain the model every quarter** using updated crash data to maintain accuracy.

---
