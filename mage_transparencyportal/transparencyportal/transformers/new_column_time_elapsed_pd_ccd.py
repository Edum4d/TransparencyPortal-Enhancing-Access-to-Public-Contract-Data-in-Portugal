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
        pandas DataFrame: The transformed DataFrame with a new column representing the number of months to sign the contract.
    """
    # Convert 'publication_date' and 'contract_conclusion_date' columns to datetime format
    data['publication_date'] = pd.to_datetime(data['publication_date'])
    data['contract_conclusion_date'] = pd.to_datetime(data['contract_conclusion_date'])
    
    # Calculate the difference in months and assign it to the new column
    data['months_to_sign_contract'] = (data['contract_conclusion_date'] - data['publication_date']) / pd.Timedelta(days=30)
    
    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert isinstance(output, pd.DataFrame), 'Output should be a DataFrame'
    
    assert 'months_to_sign_contract' in output.columns, 'DataFrame should contain the new column'
    
    # Check if the new column has numerical values
    assert output['months_to_sign_contract'].dtype in (int, float), 'The new column should contain numerical values'