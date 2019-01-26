import json
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Microsoft API Key and Link
headers = {"Ocp-Apim-Subscription-Key": 'a4cf185c040f41b19857e365d17f0c9e'}
text_analytics_sentiment_url = "https://southcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"

# Reading Data
data = pd.read_csv('./slacklogo.csv')
df = pd.DataFrame.from_dict(data.head(n=2))

# Extracting time and tweet
documents = {"documents": []}
for idx, row in df.iterrows():
    documents["documents"].append({
        "id": str(idx + 1),
        "text": row["tweet_text"],
        "time": row["timestamp"]
    })

df1 = pd.DataFrame(documents["documents"])

# Processing data
response = requests.post(text_analytics_sentiment_url,
                         headers=headers, json=documents)
sentiments = response.json()

sentiment_df = pd.DataFrame([d["score"] for d in sentiments["documents"]], index=[d["id"] for d in sentiments["documents"]],
                            columns=["sentiment_score"])
sentiment_df["sentiment_percentage"] = sentiment_df.sentiment_score * 2 - 1

for column in sentiment_df:
    df1[column] = sentiment_df[column]


print df1

# time = data['timestamp'].values
# tweets = data['tweet_text'].values
