severity_list=["Healthy","Low","Moderate","High","Critical"]
severity_score={"Healthy":95,"Low":80,"Moderate":65,"High":50,"Critical":30}
def severity_to_score(sev):
    return severity_score[sev]