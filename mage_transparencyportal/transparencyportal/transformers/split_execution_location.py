import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    # Split 'execution_location' column by '|'
    data["execution_location"] = data["execution_location"].apply(lambda x: x.split("|"))
    data = data.explode("execution_location")
    # Filter out rows where the split results in less than two elements
    data = data[data["execution_location"].apply(lambda x: len(x.split(','))) >= 2]

    # Split 'execution_location' column and assign new columns directly
    data[['country', 'city', 'parasity']] = data['execution_location'].apply(lambda x: x.split(',') + [''] * (3 - len(x.split(',')))).apply(pd.Series)
    # Drop the original 'execution_location' column
    data.drop('execution_location', axis=1, inplace=True)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
