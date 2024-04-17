import os
import pyarrow as pa
import pyarrow.parquet as pq
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS']="/home/src/env/transparencyportal-420117-da1b5becf6d6.json"
bucket_name = 'transparencyportal'
project_id= 'transparencyportal-420117'

table_name="data"

root_path=f'{bucket_name}/{table_name}'
@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """

    

    # Initialize GCS filesystem

    gcs = pa.fs.GcsFileSystem()

    # Extract year and month from the 'contract_conclusion_date' column
    df['year'] = df['contract_conclusion_date'].dt.year
    df['month'] = df['contract_conclusion_date'].dt.month

    # Convert year and month to strings with leading zeros
    df['year'] = df['year'].astype(str)
    df['month'] = df['month'].astype(str).str.zfill(2)

    # Create a new column 'partition' containing the year and month
    df['partition'] = df['year'] + '-' + df['month']
    df.drop(columns=['year', 'month'], inplace=True)

    # Write the Parquet files partitioned by year and month
    pq.write_to_dataset(
        pa.Table.from_pandas(df),
        root_path=root_path,
        partition_cols=['partition'],
        filesystem=gcs,
        basename_template='contracts-{partition}.parquet'
    )