import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data(*args, **kwargs):
    """
    Loads data from XLSX files located at the given URLs.

    Returns:
        pandas DataFrame: The concatenated data from all URLs.
    """

    urls = [
        "https://dados.gov.pt/pt/datasets/r/ff5a919e-c988-4be5-867a-3c7273f2baae",
        "https://dados.gov.pt/pt/datasets/r/f864281a-25b3-40ff-9776-1a3da76e0f5d",
        "https://dados.gov.pt/pt/datasets/r/ae8ad653-79f0-4cd4-8200-e96a12d583ee"
    ]
    dataframes = []
    for url in urls:
        try:
            # Read the XLSX file directly from the URL
            df = pd.read_excel(url, dtype={
                'idcontrato': pd.Int64Dtype(),
                'nAnuncio': str,
                'tipoContrato': str,
                'tipoprocedimento': str,
                'objectoContrato': str,
                'adjudicante': str,
                'adjudicatarios': str,
                'precoContratual': float,
                'cpv': str,
                'prazoExecucao': pd.Int64Dtype(),
                'localExecucao': str,
                'fundamentacao': str,
                'ProcedimentoCentralizado': str,
                'DescrAcordoQuadro': str,
                'Ano': pd.Int64Dtype()
            }, parse_dates=['dataPublicacao', 'dataCelebracaoContrato'], keep_default_na=False)
            dataframes.append(df)
            print(f"Sucess retrieved data from URL {url}")
        except Exception as e:
            print(f"Failed to retrieve data from URL {url}: {e}")

    return pd.concat(dataframes, ignore_index=True).dropna()

@test
def test_output(output, *args) -> None:
    """
    Test the output of the block.

    Parameters:
        output (pandas DataFrame): The concatenated data from all URLs.
    """

    expected_columns = [
        'idcontrato', 'nAnuncio', 'tipoContrato', 'tipoprocedimento', 'objectoContrato',
        'adjudicante', 'adjudicatarios', 'dataPublicacao', 'dataCelebracaoContrato',
        'precoContratual', 'cpv', 'prazoExecucao', 'localExecucao', 'fundamentacao',
        'ProcedimentoCentralizado', 'DescrAcordoQuadro', 'Ano'
    ]

    assert all(col in output.columns for col in expected_columns), "DataFrame should contain all expected columns"
    
    assert isinstance(output, pd.DataFrame), 'Output should be a DataFrame'
    