import tweepy
import tweet_dumper
import sys
import re
import json

# looks for json file with the proper credentials for the user
# {
# "consumer_key"        : "value",
# "consumer_secret"     : "value",
# "access_token"        : "value",
# "access_token_secret" : "value"
# }
def get_credentials(filename):
    with open(filename) as file:
        cfg = json.load(file)
    return cfg

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main():
    try:
        username = sys.argv[1]
        amount = int(sys.argv[2])
    except IndexError as e:
      print "Usage: python getTweets.py username amount [filename]"
      sys.exit(1)
    # Fill in the values noted in previous step here
    cfg = get_credentials("the_Tmonster.json")
    api = get_api(cfg)
    user = api.get_user(username)
    if sys.argv[3]:
      tweet_dumper.get_all_tweets4args(username, api, amount, sys.argv[3])
    else:
      tweet_dumper.get_all_tweets3args(username, api, amount)

if __name__ == "__main__":
    main()
