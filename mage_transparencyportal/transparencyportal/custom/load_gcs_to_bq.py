if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import os 
from google.cloud import bigquery
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/src/env/transparencyportal-420117-a63d0e28ae3a.json"
@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here

    job_config = bigquery.QueryJobConfig()
# Set the destination table

    sql = """create or replace external TABLE `transparencyportal-420117.final_project.test2`
OPTIONS(
 format= "parquet",
 uris=["gs://transparencyportal/data/*.parquet"]
)
    """ 
    client = bigquery.Client()

    # Start the query, passing in the extra configuration.
    query_job = client.query(
        sql,
        # Location must match that of the dataset(s) referenced in the query
        # and of the destination table.
        location='US')  # API request - starts the query

    query_job.result()  # Waits for the query to finish
    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
