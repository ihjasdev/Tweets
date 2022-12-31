import snscrape.modules.twitter as sntwitter
import pandas as pd


query ="(from:kulanthisilva) until:2022-12-31 since:2020-01-01"
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
print("-------------Converting into csv file----------")

#export the dataframe to csv file
df.to_csv(r'silva_tweets.csv', index=False)