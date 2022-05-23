# Databricks notebook source
storage_account_name=''
sas=''

# COMMAND ----------

def mount_adls(container_name):
  
    result = dbutils.fs.mount(
          source = "wasbs://{0}@{1}.blob.core.windows.net".format(container_name,storage_account_name),
          mount_point = "/mnt/sail/{0}".format(container_name),
          extra_configs = {"fs.azure.sas.{0}.{1}.blob.core.windows.net".format(container_name,storage_account_name):sas}
                        )
    if result:
      print("!! mount point:/mnt/sail/{0} is created ".format(container_name))

# COMMAND ----------

blob_containers = ["metadata", "logs", "bronze", "silver", "gold"]
try:
  for container in blob_containers:
    mount_adls(container_name=container)
except:
  raise

# COMMAND ----------

# MAGIC %fs
# MAGIC ls "/mnt/sail/silver"