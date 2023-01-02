import pandas as pd
from langdetect import detect

# Read in the CSV file
df = pd.read_csv("Tweets/lowercase.csv")

# Define a function to check if a cell contains only English
def is_english(text):
    try:
        language = detect(text)
        return language == 'en'
    except:
        return False

# Remove rows where the second column contains mixed languages
df = df[df['Tweet'].apply(is_english)]

# Save the resulting dataframe to a new CSV file
df.to_csv("Tweets/language.csv", index=False)
