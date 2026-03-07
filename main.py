from core.loader import loader
from core.profiler import profiler
from modules.completeness import completeness
#from modules.duplicates import duplicates
# from modules.outliers import outliers
# from modules.structural import struct
# from modules.validity import validity
import reporting 
import scoring

path=input("Enter your path for dataset here:")

df=loader(path)
if df is None:
    print("Dataset loading failed.")
    exit()

print("Dataset loaded successfully")
profile=profiler(df)
completeness_score=completeness(profile)
print(completeness_score)