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
        users = 1
        usernames = []
        amount = 0
        place_in_named_file = False
        for i in range(len(sys.argv)):
            try:
                # if I can cast to integer, interpret
                # as amount
                amount = int(sys.argv[users])
                break;
            except:
                # otherwise, interpret as twitterhandle
                usernames.append(sys.argv[users])
                users+=1
        if sys.argv[-2] == "-f":
            named_file = sys.argv[-1]
            place_in_named_file = True
        if len(usernames) == 0 or amount == 0:
            raise IndexError
    except IndexError as e:
      print "Usage: python getTweets.py username [username...] amount [-f filename]"
      sys.exit(1)

    # Fill in the values noted in previous step here
    cfg = get_credentials("./authentication_files/the_Tmonster.json")
    api = get_api(cfg)

    for handle in usernames:
        user = api.get_user(handle)
        if place_in_named_file:
            tweet_dumper.get_all_tweets4args(handle, api, amount, named_file)
        else:
            tweet_dumper.get_all_tweets3args(handle, api, amount)

if __name__ == "__main__":
    main()
