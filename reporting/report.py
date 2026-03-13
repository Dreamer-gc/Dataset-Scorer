def report(final_score,profile,cs,ds,vs,os):
    print("DATASET QUALITY SCORER")
    print('-'*len("DATASET QUALITY SCORER"))

    print("DATASET SUMMARY")
    print("-"*len("DATASET SUMMARY"))
    print(f"Rows: {profile['n_rows']}")
    print(f"Columns: {profile['n_cols']}\n\n")
    print(f"Numeric Columns: {profile['numeric_columns']}")
    print(f"Categorial Columns: {profile['categorial_columns']}")
    print(f"Boolean Columns: {profile['bool_columns']}")
    print(f"Datetime Columns: {profile['datetime_columns']}")

    print(f"Final Score: {final_score['final_score']}/100\nRisk Level: {final_score['risk']}\nInterpretation:\nDataset contains {final_score['risk']} quality issues")

    print("DIMENSION SCORES")
    print("-"*len("DIMENSION SCORES"))
    print(f"Completeness: {cs['score']} ({cs['severity']})")
    print(f"Validity: {vs['score']} ({vs['severity']})")
    print(f"Duplicates: {ds['score']} ({ds['severity']})")
    print(f"Outliers: {os['score']} ({os['severity']})")

    print("KEY ISSUES")
    print("-"*len("KEY ISSUES"))
    if cs['metrics']['heavy_missing_columns']:
        print("Completeness:\n\tHeavy missing values detected in:")
        for i in cs["metrices"]['heavy_missing_colunns']:
            print(f"\t\t{i}")

    if vs['invalid_columns']:
        print("Validity:\n\tInvalid values detected in:")
        for i in vs['invalid_columns']:
            print(f"\t\t{i}")
    
    if os['outlier_columns']:
        print("Outlier:\n\tExtreme values detected in:")
        for i in os['outlier_columns']:
            print(f"\t\t{i}")
