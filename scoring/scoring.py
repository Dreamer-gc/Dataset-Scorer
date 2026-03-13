from helper.helper import *
def score(cs,ds,vs,os):
    final_score=cs["score"]*weight["Completeness"]+ds["score"]*weight["Duplicate"]+vs["score"]*weight["Validity"]+os["score"]*weight["Outlier"]
    severity=[cs["severity"],ds["severity"],vs["severity"] ,os["severity"]]
    
    count=severity.count(severity_list[4])

    if count>=2:
        final_score=30
        risk=severity_list[4]
        return {
            "final_score":final_score,
            "risk":risk
        }
    elif count==1:
        final_score=50
        risk=severity_list[3]
        return {
            "final_score":final_score,
            "risk":risk
        }
    
    if cs["severity"]==severity_list[3] or vs["severity"]==severity_list[3]:
        final_score=min(final_score,84)
        risk=severity_list[3]
        return {
            "final_score":final_score,
            "risk":risk
        }
    
    if final_score >= 90:
        risk = severity_list[1]
    elif final_score >= 75:
        risk = severity_list[2]
    elif final_score >= 50:
        risk = severity_list[3]
    else:
        risk = severity_list[4]

    return {
        "final_score":final_score,
        "risk":risk
    }
        
    