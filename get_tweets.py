import snscrape.modules.twitter as sntwitter
import pandas as pd


query ="(from:jjstruthersuk) until:2022-12-31 since:2020-01-01"
tweets=[]
limit =100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets)== limit:
     break
    else:
        tweets.append([tweet.date,tweet.user.username,tweet.content])

#Put Column Name
df=pd.DataFrame(tweets, columns=['Tweet Date','User','Tweet'])

print(df)