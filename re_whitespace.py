import pandas as pd
import string

# Read in the CSV file
df = pd.read_csv("Tweets/re_empty_row.csv")

# Remove rows where the second column is empty or contains only whitespace
df = df[df['Tweet'].str.strip().ne('')]

# Save the resulting dataframe to a new CSV file
df.to_csv("Tweets/re_whitespace.csv", index=False)
