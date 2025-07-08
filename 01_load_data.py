# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Load CSV from DBFS or local path
# For local test: df = spark.read.csv('data/sample_data.csv', header=True, inferSchema=True)
df = spark.read.csv('/dbfs/FileStore/sample_data.csv', header=True, inferSchema=True)
df.show() 