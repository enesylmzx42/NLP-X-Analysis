# This is a sample Python script.

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:netflixturkiye) until:2023-01-01 since:2021-01-01"
tweets = []
limit = 5000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=["username", "tweet"])
print(df)

# to save to csv
df.to_csv('netflix_tweets.csv')
