import tweepy

access_token = "174762490-tuao9h9JUa6XLfUlI6GEccEVbws6EGqqcrR9Hagj"
access_token_secret = "ACSXh9eqjor4N1dGSs7X22AsICiwdGZxWJdBs3ISIfFxI"
consumer_key = "djrLOs8t6lcUuSVsc3XUaRcqb"
consumer_secret = "7IK64hAxDxcgHKc7KYsGGOYkGkjHOxYpwhh6hoIbXOANgu33RC"


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#Reference: Stackoverflow - This tweets the picture and the text
api.update_with_media("michigan.jpg", status="#UMSI-206 #Proj3")