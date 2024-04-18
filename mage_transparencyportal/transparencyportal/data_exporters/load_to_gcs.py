import os
import pyarrow as pa
import pyarrow.parquet as pq
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
bucket_name = os.environ.get('STORAGE_BUCKET_NAME')
project_id= os.environ.get('GCLOUD_PROJECT_NAME')

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

    output_dir = root_path

    # Write the Parquet files with partition in the filename
    for partition_value, partition_df in df.groupby('partition'):
            partition_filename = f'contracts-{partition_value}.parquet'
            # Write partitioned Parquet files
            pq.write_table(
                table=pa.Table.from_pandas(partition_df),
                where=f"{root_path}/{partition_filename}",
                filesystem=gcs
            )
