import json
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


key = 'a0d59b09-5c25-4cfd-8524-5eeeae4c4dfe'

data = pd.read_csv('./slacklogo.csv')
df = pd.DataFrame.from_dict(data)
print df.head()

# from aylienapiclient import textapi
# c = textapi.Client("f7464471", "dc1e243efba93d8019bc989a6f7a3277")
text_analytics_sentiment_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"


# date_rng = pd.date_range(start='1/16/2010', end='1/26/2018', freq='H')
# print date_rng

time = data['timestamp'].values
tweets = data['tweet_text'].values
# tweets_sentiment = map(c.Sentiment, tweets)

# print tweets_sentiment
# print time
