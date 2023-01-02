import pandas as pd

# Load the CSV file
df = pd.read_csv("Tweets\merged.csv")

# Remove the unwanted column
df = df.drop(["Tweet Date","sourcefilename"], axis=1)

# Save the modified DataFrame to a new CSV file
df.to_csv("Tweets\modified_file.csv", index=False)
