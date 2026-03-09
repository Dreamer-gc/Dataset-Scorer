from helper.helper import *
import pandas as pd
def outlier(df,profile): 
    
    outlier_ratio={}

    for col in profile["numeric_columns"]:
        outlier=[]
        values=df[col].dropna()
        q1=values.quantile(0.25)
        q3=values.quantile(0.75)
        iqr=q3-q1
        lower_bound=q1-1.5*iqr
        upper_bound=q3+1.5*iqr
        outlier = values[(values < lower_bound) | (values > upper_bound)]
        ratio=(len(outlier)/profile["n_rows"])*100
        outlier_ratio[col]=ratio
    
    if len(outlier_ratio)==0:
        return{
            "dimension": "outlier",
            "score": 100,
            "severity": "None",
            "outlier_columns": [],
            "spread_ratio": 0
        }
    outlier_cols=[key for key,val in outlier_ratio.items() if val>0]
    overall_ratio=sum(outlier_ratio.values())/len(outlier_ratio)
    
    
    spread=(len(outlier_cols)/len(profile["numeric_columns"]))*100
    if overall_ratio<=1:
        severity=severity_list[0]
    elif overall_ratio<=5:
        severity=severity_list[1]
    elif overall_ratio<=10:
        severity=severity_list[2]
    elif overall_ratio<=20:
        severity=severity_list[3]
    else:
        severity=severity_list[4]

    if 30<spread<60:
        severity=escalate(severity)
    
    if spread>=60 and severity_list.index(severity)<severity_list.index("High"):
        severity=severity_list[-2]
    
    if spread>=80 and severity_list.index(severity)<severity_list.index("Moderate"):
        severity=severity_list[-1]
    
    score=severity_to_score(severity)

    return{
        "dimension": "outlier",
        "score": score,
        "severity": severity,
        "outlier_columns": outlier_cols,
        "spread_ratio": spread
    }