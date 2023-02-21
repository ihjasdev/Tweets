

import tweepy
import json

#Authentication credentials
consumer_key = 'ibWwljH0Qa9WWqlofZ0fCP75N'
consumer_secret = 'EDlp7LtHTg3vTd5Zc0WaL4ajyDKoiuU21CGQZzQlDnD7Xygodh'
access_token = '854912607597109248-05nFjviTot90IB0xUYaLxpe9Jyjm7xE'
access_token_secret = 'WIGZUOgoF2FCNlm2C0zyOVhHWov93q8YLxZrZ9ZYlJOHK'
 
#Authenticating with the credentials 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
  
#Creating an API object to extract data from Twitter 
api = tweepy.API(auth) 

 #Login page code:

def login():

    username=input("Enter your username:")

    password=input("Enter your password:")

    if username=="admin" and password=="password":

        print("Login successful!")

        return True

    else:

        print("Incorrect username or password!")

        return False

 #Extracting recent 100 tweets of a user:    

def getTweets(username): 

    #Creating a list of tweets  

    tweets=[]  

    #Fetching the most recent 100 tweets from the user's timeline  

    newTweets=api.user_timeline(screen_name=username,count=100,tweet_mode="extended")  

    #Adding each tweet to the list of tweets  

    for tweet in newTweets:  

        tweets.append(tweet._json)  

     #Returning the list of tweets  

    return tweets