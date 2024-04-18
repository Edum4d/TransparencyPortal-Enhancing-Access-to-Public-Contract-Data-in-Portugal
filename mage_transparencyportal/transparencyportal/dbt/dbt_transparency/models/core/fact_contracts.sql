{{
    config(
        materialized='table',
        partition_by={
      "field": "publication_date",
      "data_type": "datetime",
      "granularity": "day"    },
        cluster_by=['contract_type']
    )
}}

WITH fact_contracts AS (
    SELECT  contract_id,
        notice_number,
        contract_type,
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
        framework_agreement_description
    FROM {{ ref('stg_staging__test1') }}
)

SELECT fact_contracts.* FROM fact_contracts