
# Big Data Final Project

🚗 **Title**:  
**Crash Injury Severity Prediction Using Traffic Data**

📊 **Objective**:  
Analyze traffic crash data to predict the most severe injury outcomes based on crash conditions, environment, and vehicle features.

📚 **Dataset Overview**  
- **Data Source**: City of Chicago Public Data Portal (Traffic Crashes, Vehicles, People)
- **Original Size**: 1.7+ Million records (vehicles), 1.9+ Million (people), 0.9 Million (crashes)
- **Files used**:
  - Traffic_Crashes_Vehicles.csv
  - Traffic_Crashes_Crashes.csv
  - Traffic_Crashes_People.csv

> **Note**:  
> Large raw CSVs have been excluded from this repository due to GitHub file size limits.

⚙️ **Project Structure**

| Folder / File                | Description                                      |
| ----------------------------- | ------------------------------------------------ |
| notebook.ipynb                | Main Data Analysis & Modeling Jupyter Notebook   |
| final_joined_crash_data.parquet | Final processed data (small version, Parquet format) |
| README.md                     | Project overview and instructions                |

📈 **Key Steps Performed**

- **Data Preparation**  
  - Merged Vehicles, Crashes, and People data on Crash ID.
  - Handled missing values and dropped extremely sparse columns.
  - Feature engineering: Time of crash, weather, roadway condition, vehicle type, etc.

- **Exploratory Data Analysis (EDA)**  
  - Distribution of injury severities
  - Impact of weather, lighting, and surface conditions
  - Correlation between speed limits and injury rates

- **Modeling Tasks**
  - Multi-class Classification (Injury Severity Prediction):
    - Logistic Regression
    - Decision Tree Classifier
    - Random Forest Classifier
  - Binary Classification (Fatal Crash Detection):
    - Gradient Boosted Tree Classifier

- **Model Evaluation**
  - Metrics: Accuracy, F1 Score, ROC AUC, PR AUC
  - Visualized evaluation metrics for each model

🧠 **Final Model Recommendations**

| Model                    | Task                    | Recommendation                                |
| ------------------------- | ----------------------- | --------------------------------------------- |
| Decision Tree Classifier  | Predict Injury Severity | ✅ Best multi-class performance                |
| GBT Classifier (Binary)   | Predict Fatal Crashes   | ✅ Excellent rare-event separation (ROC AUC = 0.85) |

📋 **Final Visualization**

| Model                   | Accuracy | F1 Score | ROC AUC | PR AUC |
| ------------------------ | -------- | -------- | ------- | ------ |
| Logistic Regression      | 0.8332   | 0.7781   | N/A     | N/A    |
| Decision Tree Classifier | 0.8339   | 0.7792   | N/A     | N/A    |
| Random Forest Classifier | 0.8229   | 0.7460   | N/A     | N/A    |
| GBT Classifier (Binary)  | N/A      | N/A      | 0.8543  | 0.0745 |

📦 **How to Run**

- Clone this repo:
  ```bash
  git clone https://github.com/asif-imtiaz-j/Big-Data-Project.git
  ```

- Open `notebook.ipynb` using VSCode, JupyterLab, or Databricks.

- Install required Python packages:
  ```bash
  pip install pyspark matplotlib pandas
  ```

- Run each cell to reproduce results.

---

👤 **Author**  
**Asif Imtiaz**  
Graduate Student — Business Analytics  
University of South Florida

📫 [LinkedIn](#) • [GitHub](#)
