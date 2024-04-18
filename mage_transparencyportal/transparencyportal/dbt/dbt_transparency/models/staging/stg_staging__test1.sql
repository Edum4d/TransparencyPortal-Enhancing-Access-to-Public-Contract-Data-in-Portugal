WITH source AS (
    SELECT * FROM {{ source('staging', 'test1') }}
),
renamed AS (
    SELECT
        {{ dbt.safe_cast("contract_id", api.Column.translate_type("integer")) }} AS contract_id,
        notice_number AS notice_number,
        contract_type AS contract_type,
        procedure_type AS procedure_type,
        contract_object AS contract_object,
        contracting_authority AS contracting_authority,
        contractors AS contractors,
        cast(publication_date as datetime)  AS publication_date,
        cast(contract_conclusion_date as datetime)  AS contract_conclusion_date,
        {{ dbt.safe_cast("contract_price", api.Column.translate_type("numeric")) }} AS contract_price,
        cpv_code AS cpv_code,
        {{ dbt.safe_cast("execution_period", api.Column.translate_type("integer")) }} AS execution_period,
        TRIM(country) AS country,
        TRIM(district) AS district,
        TRIM(city) AS city,
        justification AS justification,
        centralized_procedure AS centralized_procedure,
        framework_agreement_description AS framework_agreement_description
    FROM source
)
SELECT 
    contract_id,
    notice_number,
    TRIM(split_column) AS contract_type,
    procedure_type,
    contract_object,
    contracting_authority,
    contractors,
    publication_date,
    contract_conclusion_date,
    contract_price,
    cpv_code,
    execution_period,
    country,
    district,
    city,
    justification,
    centralized_procedure,
    CASE
        WHEN framework_agreement_description = 'NULL' THEN ''
        ELSE framework_agreement_description
    END AS framework_agreement_description
FROM renamed,
UNNEST(SPLIT(contract_type, '|')) AS split_column


-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=false) %}

  limit 100

{% endif %}