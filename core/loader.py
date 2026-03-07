import pandas as pd
import os
supported_ext=[".csv",".xlsx"]
def loader(path):
    try:
        ext=os.path.splitext(path)[1].lower()
        if ext in supported_ext:
            if ext==".csv":
                df=pd.read_csv(path)

            else:
                df=pd.read_excel(path)
                
            return df
        else:
            print("Unsupported file type.")
        
    except pd.errors.ParserError:
        print("Parsing error.")

    except pd.errors.EmptyDataError:
        print("Empty file.")

    except FileNotFoundError:
        print("File not found at that location.")