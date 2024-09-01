-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### Create Cataloge

-- COMMAND ----------

CREATE CATALOG IF NOT EXISTS catalog_formula1 MANAGED LOCATION 'abfss://demo@exucdatabricks.dfs.core.windows.net/';


-- COMMAND ----------

USE CATALOG catalog_formula1 ;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Create Schema

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS bronze
MANAGED LOCATION 'abfss://bronze@exucdatabricks.dfs.core.windows.net/'

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS silver
MANAGED LOCATION 'abfss://silver@exucdatabricks.dfs.core.windows.net/'

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS gold
MANAGED LOCATION 'abfss://gold@exucdatabricks.dfs.core.windows.net/'

-- COMMAND ----------

