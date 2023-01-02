import pandas as pd
import string

# Read in the CSV file
df = pd.read_csv("Tweets/re_duplicate.csv")

# Convert all cells to lowercase
df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# Save the resulting dataframe to a new CSV file
df.to_csv("Tweets/lowercase.csv", index=False)
