import pandas as pd

# Read in the CSV file
df = pd.read_csv("Tweets/re_whitespace.csv")

# Remove duplicate rows based on the values in the second column
df = df.drop_duplicates(subset=['Tweet'])

# Save the resulting dataframe to a new CSV file
df.to_csv("Tweets/re_duplicate.csv", index=False)
