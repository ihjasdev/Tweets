import pandas as pd

# Read in the CSV file
df = pd.read_csv("Tweets/remove_char_file.csv")

# Remove rows where the second column is empty
df = df[df['Tweet'].notna()]

# Save the resulting dataframe to a new CSV file
df.to_csv("Tweets/re_empty_row.csv", index=False)
