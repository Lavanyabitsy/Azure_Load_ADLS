# Databricks notebook source
# Set your ADLS path
output_path = "abfss://<container>@<storage_account>.dfs.core.windows.net/output/"

# Assume df_transformed is available from previous step
# df_transformed.write.mode("overwrite").parquet(output_path)

if 'df_transformed' in locals():
    df_transformed.write.mode("overwrite").parquet(output_path)
    print(f"Data written to {output_path}")
else:
    print('Transformed DataFrame not found. Please run the previous notebook or transform the data.') 