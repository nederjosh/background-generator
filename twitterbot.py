import tweepy
import time
#testing modifying
auth = tweepy.OAuthHandler('DtxjkdB2Ur0avpK1bBcccv8e6', '1mwCJweNHvJ53fdYivedOTkiah58p3wnSFZt9n9AA429SOK3ee')
auth.set_access_token('1404968891776860163-AMvtJwJqenjio3L8D81TYr7L8ryKvK', 'cRIY7I0Nc2Gsu8EbNUD9C8p6vhk6aKwFM9SdweEut1T7K')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(1000)


search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
	try:
		tweet.favorite()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

'''
#generousbot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	if follower.name == 'SteveMartinToGo':
		follower.follow()
		break
'''


'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)

'''