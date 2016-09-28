import dataset

import tweepy
import dataset
from textblob import TextBlob

db = dataset.connect("sqlite:///tweets.db")

result = db["tweets"].all()

dataset.freeze(result, format='csv', filename='results.csv')