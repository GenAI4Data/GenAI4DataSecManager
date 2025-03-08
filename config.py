# Use a configuration class or dictionary for better organization
class Config:
    PROJECT_ID = 'ce-sap-latam-test-deploy'
    RLS_MANAGER_DATASET = 'rls_security'
    POLICY_TABLE = f'{PROJECT_ID}.{RLS_MANAGER_DATASET}.policies'
    FILTER_TABLE = f'{PROJECT_ID}.{RLS_MANAGER_DATASET}.policies_filters'