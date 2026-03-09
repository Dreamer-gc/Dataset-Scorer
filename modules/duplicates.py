
from rules.rules import *
def duplicates(profile):
    
    if profile["n_rows"]==0:
        duplicate_percentage=0
    else:
        duplicate_percentage=(profile["n_duplicate"]/profile["n_rows"])*100
    
    if(duplicate_percentage==0):
        severity=severity_list[0]
    elif(duplicate_percentage>0 and duplicate_percentage<=2):
        severity=severity_list[1]        
    elif(duplicate_percentage>2 and duplicate_percentage<=5):
        severity=severity_list[2]
    elif(duplicate_percentage>5 and duplicate_percentage<=15):
        severity=severity_list[3]
    elif(duplicate_percentage>15):
        severity=severity_list[4]
    
    score=severity_to_score(severity)
    
    return {
        "dimesnsion":"Duplicates",
        "score":score,
        "severity":severity,
        "duplicate_rows_percentage":duplicate_percentage
    }