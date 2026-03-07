import pandas as pd
def profiler(df):
    n_rows=df.shape[0]
    n_cols=df.shape[1]
    data_types=df.dtypes
    count_missing_values=df.isnull().sum()
    count_unique_values=df.nunique()
    numeric_cols=df.select_dtypes(include=['int64','float64']).columns
    cat_cols=df.select_dtypes(include=['object','category']).columns
    n_duplicate=df[df.duplicated()].sum()
    return {
        "n_rows":n_rows,
        "n_cols":n_cols,
        "dtypes":data_types,
        "n_missing":count_missing_values,
        "n_unique":count_unique_values,
        "numeric_columns":numeric_cols,
        "categorial_columns":cat_cols,
        "n_duplicate":n_duplicate
    }