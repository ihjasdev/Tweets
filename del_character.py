import pandas as pd
import re

# Read in the CSV file
df = pd.read_csv("Tweets/new_file.csv")

# Remove special characters
df = df.applymap(lambda x: re.sub(r'[^\w\s]', '', x))

# Remove URLs
df = df.applymap(lambda x: re.sub(r'https?:\/\/.*[\r\n]*', '', x))

# Save the resulting dataframe to a new CSV file
df.to_csv("Tweets/del_char_file.csv", index=False)
