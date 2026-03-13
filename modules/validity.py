import pandas as pd
from helper.helper import *
def validity(df,profile):
    invalid_columns=set()
    invalid_ratios={}

    for col in profile["numeric_columns"]:
        convert=pd.to_numeric(df[col],errors="coerce")
        invalid=convert.isna() & df[col].notna()
        invalid_count=invalid.sum()

        ratio=invalid_count/profile["n_rows"]

        if ratio>0:
            invalid_columns.add(col)
        invalid_ratios[col]=ratio
    
    for col in profile["datetime_columns"]:
        convert=pd.to_datetime(df[col],errors="coerce")
        invalid=convert.isna() &df[col].notna()
        invalid_count=invalid.sum()
        
        ratio=invalid_count/profile["n_rows"]

        if ratio>0:
            invalid_columns.add(col)
        invalid_ratios[col]=ratio
    
    for col in profile["categorial_columns"]:
        numeric_invalid=pd.to_numeric(df[col],errors="coerce")
        invalid=numeric_invalid.notna()
        n_count=invalid.sum()
        n_ratio=n_count/profile["n_rows"]
        space_invalid=df[col].astype(str).str.isspace().sum()
        s_ratio=space_invalid/profile["n_rows"]
        ratio=(s_ratio+n_ratio)/2
        if ratio>0:
            invalid_columns.add(col)
        invalid_ratios[col]=ratio
    
    spread_ratio=len(invalid_columns)/profile["n_cols"]
    max_invalid=(max(invalid_ratios.values()))*100 if invalid_ratios else 0

    if max_invalid==0:
        severity=severity_list[0]
    elif max_invalid<=5:
        severity=severity_list[1]
    elif max_invalid<=15:
        severity=severity_list[2]
    elif max_invalid<=30:
        severity=severity_list[3]
    else:
        severity=severity_list[4]

    score=severity_to_score(severity)

    return {
        "dimension": "validity",
        "score": score,
        "severity": severity,
        "invalid_columns": list(invalid_columns),
        "spread_ratio": spread_ratio
    }