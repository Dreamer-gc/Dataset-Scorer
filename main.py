from core.loader import loader
from core.profiler import profiler
from modules.completeness import completeness
from modules.duplicates import duplicates
from modules.outliers import outlier
from modules.validity import validity
from scoring.scoring import score

path=input("Enter your path for dataset here:")

df=loader(path)
if df is None:
    print("Dataset loading failed.")
    exit()

print("Dataset loaded successfully")
profile=profiler(df)
completeness_score=completeness(profile)
duplicates_score=duplicates(profile)
validity_score=validity(df,profile)
outlier_score=outlier(df,profile)

final_score=score(completeness_score,duplicates_score,validity_score,outlier_score)