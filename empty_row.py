import pandas as pd

# Read in the CSV file
df = pd.read_csv("Tweets/remove_char_file.csv")

# Remove rows where all cells are empty
df = df.dropna(how='all')

# Save the resulting dataframe to a new CSV file
df.to_csv("re_empty_row.csv", index=False)
