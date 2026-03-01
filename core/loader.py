# 1️⃣ File Validation

# Before loading:

# Does file exist?

# Is it readable?

# Is extension supported?

# Is file empty?

# If any fails → raise clear error.

# Loader should fail fast.

# 2️⃣ Supported File Formats

# For Version 1, support:

# .csv

# .xlsx (optional)

# Check file extension.

# Do NOT try to detect format magically.

# Be explicit.

# 3️⃣ Safe Reading

# Loader should:

# Read file into DataFrame

# Catch parsing errors

# Handle encoding issues safely

# Return dataframe

# No transformations.

# No cleaning.

# 4️⃣ Basic Structural Checks

# After loading:

# Check:

# Rows > 0

# Columns > 0

# No completely duplicate column names

# Column names are valid strings

# These are structural checks, not quality checks.

# 5️⃣ Metadata Output

# Loader should return:

# DataFrame

# Basic metadata (optional)

# Example conceptual output:

# {
#     "dataframe": df,
#     "row_count": n_rows,
#     "column_count": n_columns,
#     "column_names": [...]
# }

# Even if you only return df,
# at least compute row/column count inside loader