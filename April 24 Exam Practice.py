# Databricks notebook source

file_location = "/FileStore/tables/gun_violence_data_01_2013_03_2018.csv"
file_type = "csv"

# CSV options
infer_schema = "True"
first_row_is_header = "True"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format("csv") \
  .option("header", "true") \
  .option("inferSchema", "true") \
  .option("sep", ",") \
  .load(file_location)

display(df)

# COMMAND ----------

temp_table_name = "gun_violence"

df.createOrReplaceTempView(temp_table_name)
display(df)

# COMMAND ----------

spark.sql("""
SELECT COUNT(*) AS total_incidents
FROM gun_violence
""").show()

# COMMAND ----------

spark.sql("""
SELECT SUM(n_killed) AS total_killed
FROM gun_violence
""").show()

# COMMAND ----------

spark.sql("""
SELECT state, COUNT(*) AS incident_count
FROM gun_violence
GROUP BY state
ORDER BY incident_count DESC
LIMIT 5
""").show()

# COMMAND ----------

spark.sql("""
SELECT state, SUM(n_killed) AS total_killed
FROM gun_violence
GROUP BY state
ORDER BY total_killed DESC
LIMIT 5
""").show()