from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from google.cloud import storage
import pandas as pd
from os import path
import os
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    """
    Template for loading data from a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/src/env/transparencyportal-420117-a63d0e28ae3a.json"
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    bucket_name = 'transparencyportal'
    object_key = 'data'
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    


    dfs = []
    for blob in bucket.list_blobs(prefix=object_key):
        if blob.name.endswith(".parquet"):
            GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).load(
                bucket_name,
                object_key+"/"+blob.name,
            )
            df = pd.read_parquet(f"gs://{bucket_name}/{blob.name}")
            dfs.append(df)

    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
