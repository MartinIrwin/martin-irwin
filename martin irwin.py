import json

with open('output.json', 'r', encoding='utf8', errors='ignore') as json_file:  
    data = json.load(json_file)
    for tweet in data:
      if "WALL" in tweet["text"]:
        print("Created at:", tweet['created_at'])
        print("Tweet:", tweet['text'])
        print(tweet['user']['name'])
        print()


import tweepy
import json
import pprint
from tweepy import OAuthHandler
consumer_key = '1hwCUHMIrEsVUAL61cZgvT1eK'
consumer_secret = 'plKB6rUOrP7lvAuVZV0LNls5j35wcwCcIAvL4gndvTH6WAZHjv'
access_token = '1089558844223774723-Sh9wU1xrGC9mJXE2zccgjPW39OBw1z'
access_secret = '5CuDwrlIS52Q6JTaEcnrIwOfyHXLG6BAgZAL7xwhcyQQF'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
api = tweepy.API(auth_handler=auth, parser=tweepy.parsers.JSONParser())
 
 
# We create a tweet list as follows:
tweets = api.user_timeline(screen_name="wearemessi", count=200)
#pprint.pprint(tweets)
 
with open("output.json", "w") as f:
 f.write(json.dumps(tweets))
 
print("Number of tweets extracted: {}.\n".format(len(tweets)))


with open("hey.txt","r") as f:
 for line in f:
   print(line)
   
   with open (“myfile.txt”, “r”) as f:
    for line in f:
        print(line)


