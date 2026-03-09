import pandas as pd
severity_list=["Healthy","Low","Moderate","High","Critical"]
severity_score={"Healthy":95,"Low":80,"Moderate":65,"High":50,"Critical":30}
def severity_to_score(sev):
    return severity_score[sev]

def detect_bool(df, object_cols):
    patterns=["true","false","yes","no","y","n","0","1"]
    bool_cols=[]

    for col in object_cols:
        values=df[col].dropna().astype(str).str.lower().unique()

        if len(values)<=3 and set(values).issubset(patterns):
            bool_cols.append(col)
    
    return bool_cols
def detect_date(df, object_cols):
    datetime_cols=[]
    for col in object_cols:
        converted=pd.to_datetime(df[col],errors="coerce")

        success_ratio=converted.notna().sum()/len(df[col])

        if success_ratio>0.9:
            datetime_cols.append(col)
    return datetime_cols

def escalate(severity):
        idx = severity_list.index(severity)
        if idx < len(severity_list) - 1:
            return severity_list[idx + 1]
        return severity