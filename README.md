# Big-Data-Project


Data Sets: 
https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/data_preview
https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d/data_preview
https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3/data_preview


---

## 📊 EDA and Modeling Direction (by Asif)

This section covers the exploratory data analysis (EDA) and initial modeling preparation for the project.

### ✅ Tasks Completed:
- Loaded and joined three datasets from the City of Chicago Open Data Portal:
  - Traffic Crashes (Crashes)
  - Traffic Crashes (Vehicles)
  - Traffic Crashes (People)
- Cleaned and merged datasets using `CRASH_RECORD_ID` and `VEHICLE_ID`
- Conducted null value analysis and feature quality assessment
- Identified high-value predictive features (e.g., weather condition, lighting, vehicle type, crash hour)
- Explored class distribution for injury severity (`MOST_SEVERE_INJURY`)
- Analyzed distribution of total injuries per crash (`INJURIES_TOTAL`)
- Created a cleaned and trimmed modeling-ready dataset

### 🧠 Suggested Modeling Direction:
> **Research Question:**  
> Can we predict the most severe injury outcome of a crash based on crash conditions, environment, and vehicle type?

| Direction              | Target Variable           | Rationale                                           |
|------------------------|---------------------------|-----------------------------------------------------|
| ✅ Multi-class Classification | `MOST_SEVERE_INJURY`        | Balanced class distribution and interpretability     |
| Binary Classification   | `INJURIES_FATAL` (0/1)     | Predicting fatal crashes (rare but meaningful)       |
| Regression              | `INJURIES_TOTAL`           | Less preferred due to skewed distribution            |

### 💾 Output:
- Final modeling dataset saved as Parquet file
- Notebook: [`EDA_Modeling_Direction.ipynb`](notebook/EDA_Modeling_Direction.ipynb)
