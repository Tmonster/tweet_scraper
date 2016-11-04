import tweepy
import tweet_dumper
import sys
import re

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main():
    if sys.argv[1] and sys.argv[2]:
        username = sys.argv[1]
        amount = int(sys.argv[2])
    else:
      print "Usage: python trumTweets.py username amount [filename]"
      sys.exit(1)
    # Fill in the values noted in previous step here
    cfg = {
    "consumer_key"        : "Ximk8dlrGGejLqL65TO39SqMD",
    "consumer_secret"     : "SiwVIoNUygs8FdZRAb4D3n6IdQUYPfUG82UNu2OwWUFhO9fq0l",
    "access_token"        : "705285627-hsGmup5zp84eZ6BPCqjmAWaR3g2YOXad3gPBnUac",
    "access_token_secret" : "Z6ws8O78em89H4ErpD5O2A0UM90t7hBXLxXRVH2Rson6V"
    }

    api = get_api(cfg)
    user = api.get_user("realDonaldTrump")
    if sys.argv[3]:
      tweet_dumper.get_all_tweets(username, api, amount, sys.argv[3]+".txt")
    else:
      tweet_dumper.get_all_tweets(username, api, amount)

if __name__ == "__main__":
  main()
