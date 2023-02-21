import json
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Read the JSON file into a list of dictionaries
with open('Tweets/total tweets.json') as f:
    tweets = json.load(f)

stop_words = set(stopwords.words('english'))

def preprocess(text):
    # Remove unwanted characters
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize the text
    words = word_tokenize(text)
    # Remove stop words
    words = [word for word in words if word.lower() not in stop_words]
    return words

# Iterate through the tweets
for tweet in tweets:
    # Extract the tweets text
    tweets_text = tweet['tweets'] 
    # Preprocess the tweets text
    tweets_text = preprocess(tweets_text)
    # Replace the original tweets text with the preprocessed tweets text
    tweet['tweets'] = tweets_text
