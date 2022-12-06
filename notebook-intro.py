# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook Introduction
# MAGIC * UI Intro
# MAGIC * Magic Comments
# MAGIC * %sql
# MAGIC * %r
# MAGIC * %md
# MAGIC * %fs
# MAGIC * %sh

# COMMAND ----------

print("hello world...")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello"

# COMMAND ----------

# MAGIC %r
# MAGIC print("hello")

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /databricks-datasets/COVID/covid-19-data/excess-deaths/deaths.csv

# COMMAND ----------

# MAGIC %sh
# MAGIC ps
