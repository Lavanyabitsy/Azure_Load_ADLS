# Databricks notebook source
from pyspark.sql.functions import col

# Assume df is loaded from previous step or reload here
# df = spark.read.csv('/dbfs/FileStore/sample_data.csv', header=True, inferSchema=True)

# Example transformation: double the amount
if 'df' in locals():
    df_transformed = df.withColumn('amount_doubled', col('amount') * 2)
    df_transformed.show()
else:
    print('DataFrame df not found. Please run the previous notebook or load the data.') 