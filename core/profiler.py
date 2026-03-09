from helper.helper import*
def profiler(df):
    n_rows=df.shape[0]
    n_cols=df.shape[1]
    data_types=df.dtypes
    count_missing_values=df.isnull().sum()
    count_unique_values=df.nunique()
    numeric_cols=df.select_dtypes(include=['int64','float64']).columns.tolist()
    cat_cols=df.select_dtypes(include=['object','category']).columns.tolist()
    bool_cols=detect_bool(df,cat_cols)
    remaining_col=[col for col in cat_cols if col not in bool_cols]
    datetime_cols=detect_date(df,cat_cols)
    cat_cols=[col for col in remaining_col if col not in datetime_cols]
    n_duplicate=df[df.duplicated()].sum()
    return {
        "n_rows":n_rows,
        "n_cols":n_cols,
        "dtypes":data_types,
        "n_missing":count_missing_values,
        "n_unique":count_unique_values,
        "numeric_columns":numeric_cols,
        "categorial_columns":cat_cols,
        "bool_columns":bool_cols,
        "datetime_columns":datetime_cols,
        "n_duplicate":n_duplicate
    }