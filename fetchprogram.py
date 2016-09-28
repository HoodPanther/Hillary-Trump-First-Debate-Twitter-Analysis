import requests
import tweepy
from textblob import TextBlob
import textblob
import dataset
import json

TWITTER_APP_KEY =  "w1FU6mBiSDCh5vvQw93maL4Ar"
TWITTER_APP_SECRET = "ShvAvuh91vKKIfnjA7DchDmN7eSR4kHFQC6RJx5VtJTjppsny1"

TWITTER_KEY =  "34191911-aytuEY7N6BXflsXv0UbLD31pc1GIkN8EAmb8T3PGy"
TWITTER_SECRET =  "3635DooRvx6LUEmUxKw2rw0LY6sKYJdpiW9oy78dGVV0p"

# esp = self.session.request('POST',
#                             url,
#                             data=self.body,
#                             timeout=self.timeout,
#                             stream=True,
#                             auth=auth,
#                             verify=self.verify)

db = dataset.connect("sqlite:///tweets.db")

auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):

	def on_status(self, status):
		if status.retweeted:
			return

		description = status.user.description
		loc = status.user.location
		text = status.text
		coords = status.coordinates
		name = status.user.screen_name
		user_created = status.user.created_at
		followers = status.user.followers_count
		id_str = status.id_str
		created = status.created_at
		retweets = status.retweet_count
		bg_color = status.user.profile_background_color
		geo=status.geo

		blob = TextBlob(text) #Initialize Blob class
		sent = blob.sentiment #Grab Sentiment object
		polarity = sent.polarity
		subjectivity = sent.subjectivity

		if geo is not None:
			geo = json.dumps(geo)

		if coords is not None:
			 coords = json.dumps(coords)

		table = db["tweets"]
		try:
			table.insert(dict(
	    		user_description=description,
			    user_location=loc,
			    coordinates=coords,
			    text=text,
			    user_name=name,
			    user_created=user_created,
			    user_followers=followers,
			    id_str=id_str,
			    created=created,
			    retweet_count=retweets,
			    user_bg_color=bg_color,
			    polarity=sent.polarity,
			    subjectivity=sent.subjectivity,
			))
		except ProgrammingError as err:
			print(err)
		print(status.text)

	def on_error(self, status_code):
		if status_code == 420:
			return False

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["trump", "clinton", "hillary clinton", "donald trump"])