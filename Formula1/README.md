# Azure Databricks Formula 1 Project

## Project Overview

This project is focused on analyzing Formula 1 race data using Azure Databricks. The goal is to process and analyze the data using various Azure technologies, enabling efficient data handling and insights extraction.

## Project Architecture

![Dataset Graph](./final.png)


## Dataset
The dataset includes historical Formula 1 data, such as race results, driver standings, and lap times. The data is processed to gain insights into team performance, driver comparisons, and race outcomes.

### Dataset Graph
![Dataset Graph](./RawDataSets/ergast_db.png)

## Technologies Used

The project leverages the following Azure services and technologies:

# Azure Databricks Formula 1 Project

## Technologies Used

- <span style="color:read;">**Azure Databricks**</span>: For big data processing and analysis.
- <span style="color:blue;">**Service Principal Access**</span>: To securely authenticate and access Azure resources.
- <span style="color:blue;">**Azure Mount**</span>: To mount Azure Data Lake Storage (ADLS) in Databricks for seamless data access.
- <span style="color:blue;">**External Tables**</span>: For querying data stored outside of Databricks.
- <span style="color:blue;">**Managed Tables**</span>: For storing and managing data within Databricks.
- <span style="color:blue;">**Incremental Load**</span>: For loading data incrementally, ensuring efficient data processing.
- <span style="color:blue;">**Full Load**</span>: For loading complete datasets in a single operation.
- <span style="color:blue;">**Delta Lake**</span>: For handling large-scale data with ACID transactions and scalable metadata handling.
- <span style="color:blue;">**Azure Key Vault**</span>: For securely storing and accessing secrets like connection strings and credentials.
- <span style="color:blue;">**Azure Data Factory**</span>: For orchestrating data pipelines and automating data movement.
- <span style="color:blue;">**Unity Catalog**</span>: This option (in this project) is for centralized management and governance of data and metadata across Databricks.


## Project Setup

### Prerequisites

- An active Azure subscription.
- Azure Databricks workspace.
- Azure Data Lake Storage (ADLS) account.
- Azure Key Vault for secure secret management.
- Azure Data Factory instance for data pipeline orchestration.

