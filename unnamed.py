import pandas as pd

# Read in the CSV file
df = pd.read_csv("Tweets/modified_file.csv")

# Drop the unnamed column
df = df.drop(df.columns[df.columns.str.contains('Unnamed', case=False)], axis=1)

# Save the resulting dataframe to a new CSV file
df.to_csv("Tweets/re_unnamed.csv", index=False)
