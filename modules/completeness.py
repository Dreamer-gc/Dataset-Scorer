
from rules.rules import *
def completeness(profile):
    missing_percentage=(profile["n_missing"]/profile["n_rows"])*100
    missing_percentage_overall=(profile["n_missing"].sum()/(profile["n_rows"]*profile["n_cols"]))*100
    
    low_missing_columns=missing_percentage[(missing_percentage>5) & (missing_percentage<=15)].index.tolist()
    moderate_missing_columns=missing_percentage[(missing_percentage>15) & (missing_percentage<=30)].index.tolist()
    heavily_missing_columns=missing_percentage[(missing_percentage>30) & (missing_percentage<=50)].index.tolist()
    critical_missing_columns=missing_percentage[missing_percentage>50].index.tolist()
    
    spread = ((len(heavily_missing_columns) + len(critical_missing_columns)) / profile["n_cols"]) * 100
    
    if critical_missing_columns:
        severity=severity_list[4]
    elif heavily_missing_columns:
        severity=severity_list[3]
    elif moderate_missing_columns:
        severity=severity_list[2]
    elif low_missing_columns:
        severity=severity_list[1]
    else:
        severity=severity_list[0]
    
    def escalate(severity):
        idx = severity_list.index(severity)
        if idx < len(severity_list) - 1:
            return severity_list[idx + 1]
        return severity

    if spread>=30:
        severity=escalate(severity)
    
    if spread>=60 and severity_list.index(severity)<severity_list.index("High"):
        severity=severity_list[-2]
    
    if spread>=80 and severity_list.index(severity)<severity_list.index("Moderate"):
        severity=severity_list[-1]

    score=severity_to_score(severity)
    issues = []

    if heavily_missing_columns:
        issues.append(f"{len(heavily_missing_columns)} columns contain heavy missing values")

    if critical_missing_columns:
        issues.append(f"{len(critical_missing_columns)} columns contain critical missing values")
    return {
        "dimension": "completeness",
        "score":score,
        "severity":severity,
        "metrics":{
            "overall_missing":missing_percentage_overall,
            "heavy_missing_columns": heavily_missing_columns,
            "spread":spread
        },
        "issues":issues        
    }