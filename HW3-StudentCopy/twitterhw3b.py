import tweepy
from textblob import TextBlob

access_token = "174762490-tuao9h9JUa6XLfUlI6GEccEVbws6EGqqcrR9Hagj"
access_token_secret = "ACSXh9eqjor4N1dGSs7X22AsICiwdGZxWJdBs3ISIfFxI"
consumer_key = "djrLOs8t6lcUuSVsc3XUaRcqb"
consumer_secret = "7IK64hAxDxcgHKc7KYsGGOYkGkjHOxYpwhh6hoIbXOANgu33RC"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#search for tweets with election
public_tweets = api.search('election')

#sum of the sentiment analysis and also a counter to get the average
sum_subjectivity = 0
sum_polarity = 0
counter = 0

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	sum_subjectivity = sum_subjectivity + analysis.sentiment.subjectivity 
	sum_polarity = sum_polarity + analysis.sentiment.polarity
	counter += 1


#Calculates and prints the average of subjetivity and polarity
print("Average subjectivity is " + str(sum_subjectivity/counter))
print("Average polarity is " + str(sum_polarity/counter) )
