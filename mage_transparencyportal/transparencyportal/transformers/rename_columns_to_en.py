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
        pandas DataFrame: The transformed DataFrame with columns renamed to English.
    """
    # Specify column name translations
    column_translations = {
        'idcontrato': 'contract_id',
        'nAnuncio': 'notice_number',
        'tipoContrato': 'contract_type',
        'tipoprocedimento': 'procedure_type',
        'objectoContrato': 'contract_object',
        'adjudicante': 'contracting_authority',
        'adjudicatarios': 'contractors',
        'dataPublicacao': 'publication_date',
        'dataCelebracaoContrato': 'contract_conclusion_date',
        'precoContratual': 'contract_price',
        'cpv': 'cpv_code',
        'prazoExecucao': 'execution_period',
        'localExecucao': 'execution_location',
        'fundamentacao': 'justification',
        'ProcedimentoCentralizado': 'centralized_procedure',
        'DescrAcordoQuadro': 'framework_agreement_description',
        'Ano': 'year'
    }
    
    # Rename columns
    data = data.rename(columns=column_translations)

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert isinstance(output, pd.DataFrame), 'Output should be a DataFrame'
    
    expected_columns = [
        'contract_id', 'notice_number', 'contract_type', 'procedure_type', 'contract_object',
        'contracting_authority', 'contractors', 'publication_date', 'contract_conclusion_date',
        'contract_price', 'cpv_code', 'execution_period', 'execution_location', 'justification',
        'centralized_procedure', 'framework_agreement_description', 'year'
    ]
    assert all(col in output.columns for col in expected_columns), 'DataFrame should contain all expected columns'