# Databricks notebook source
#### If you have a subscription account on azure i recommend using mount Data Lake using_service
### If don't have a subscription  account and used azure student account recommend using Cluster scope authentication and abfss protocol

# COMMAND ----------

def mount_adls(storage_account_name,continer_name):
    # Get secrets from Key Vault
    client_id = dbutils.secrets.get(scope = 'formula1-scope', key = 'formula1-app-client-id')
    tenant_id = dbutils.secrets.get(scope = 'formula1-scope', key = 'formula1-app-tenant-id')
    client_secret = dbutils.secrets.get(scope = 'formula1-scope', key = 'formula1-app-client-secret')

    # Set spark configurations
    configs = {"fs.azure.account.auth.type": "OAuth",
              "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
              "fs.azure.account.oauth2.client.id": client_id,
              "fs.azure.account.oauth2.client.secret": client_secret,
              "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}
    # Unmount the mount point if it already exists
    if any(mount.mountPoint == f"/mnt/{storage_account_name}/{continer_name}" for mount in dbutils.fs.mounts()):
        dbutils.fs.unmount(f"/mnt/{storage_account_name}/{continer_name}")
    
    # Mount the storage account container
    dbutils.fs.mount(
      source = f"abfss://{continer_name}@{storage_account_name}.dfs.core.windows.net/",
      mount_point = f"/mnt/{storage_account_name}/{continer_name}",
      extra_configs = configs)
    
    display(dbutils.fs.mounts())

# COMMAND ----------

# Mount Raw Container
mount_adls('projectformula1id', 'raw')

# Mount processed Container

mount_adls('projectformula1id', 'processed')

# Mount presentation Container

mount_adls('projectformula1id', 'presentation')

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

