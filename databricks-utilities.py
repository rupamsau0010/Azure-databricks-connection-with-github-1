# Databricks notebook source
# MAGIC %md
# MAGIC # Utilities in Databricks
# MAGIC * File system utilities
# MAGIC * Notebook workflow utilities
# MAGIC * Widget utilities
# MAGIC * Secret utilities
# MAGIC * Library utilities

# COMMAND ----------

# MAGIC %fs
# MAGIC ls

# COMMAND ----------

dbutils.fs.ls("/")

# COMMAND ----------

for folder_name in dbutils.fs.ls("/"):
    print(folder_name)

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.help("mount")

# COMMAND ----------

dbutils.notebook.help()

# COMMAND ----------

dbutils.notebook.run("./child-notebook", 10)

# COMMAND ----------

dbutils.widgets.help()

# COMMAND ----------

dbutils.notebook.run("./child-notebook", 10, {"input": "From the child notebook"})

# COMMAND ----------

# MAGIC %pip install numpy
