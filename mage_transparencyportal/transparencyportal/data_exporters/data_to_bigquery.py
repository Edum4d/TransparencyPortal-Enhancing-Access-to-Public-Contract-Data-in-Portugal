from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path
import os
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    from pyspark.sql import SparkSession

    # Import necessary libraries for BigQuery
    from google.cloud import bigquery
    from google.oauth2 import service_account

    # Set up the service account credentials
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']="/home/src/env/transparencyportal-420117-da1b5becf6d6.json"

    # Initialize the Spark session
    spark = SparkSession.builder \
        .appName("PySpark to BigQuery") \
        .config('spark.jars', 'gs://spark-lib/bigquery/spark-bigquery-latest.jar') 
        .getOrCreate()

    # Create a DataFrame (Replace this with your actual DataFrame)
    # For example:
    # df = spark.createDataFrame([(1, 'John', 25), (2, 'Alice', 30)], ['id', 'name', 'age'])

    # Define BigQuery options
    table_id = "transparencyportal-420117.final_project.transparencyportal_data"
    project_id = "transparencyportal-420117"

    # Write data to BigQuery
    spark.createDataFrame(df).write \
        .format("bigquery") \
        .option("temporaryGcsBucket", "transparencyportal-420117") \
        .option("table", table_id) \
        .option("project", project_id) \
        .mode("append") \
        .save()

    # Stop Spark session
    spark.stop()
