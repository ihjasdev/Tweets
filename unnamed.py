import pandas as pd

# Read in the CSV file
df = pd.read_csv("Tweets/modified_file.csv")

# Drop the unnamed column
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Save the resulting dataframe to a new CSV file
df.to_csv("Tweets/new_file.csv", index=False)
