-- Databricks notebook source
CREATE EXTERNAL LOCATION IF NOT EXISTS external_bronze
URL 'abfss://bronze@exucdatabricks.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL `databricksource_ex_storage_credential`)

-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS external_silver
URL 'abfss://silver@exucdatabricks.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL `databricksource_ex_storage_credential`)

-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS external_gold
URL 'abfss://gold@exucdatabricks.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL `databricksource_ex_storage_credential`)

-- COMMAND ----------

