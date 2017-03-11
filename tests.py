import tweepy #https://github.com/tweepy/tweepy
import os
import filecmp
import tweet_dumper
import json

# For twitter account @TestsssTom
# Password to account is "saymanyougottajoint"
# key management
# https://apps.twitter.com/app/13524605/keys

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


def batch_delete(api):
    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
        except:
            print "Failed to delete:", status.id

def batch_tweet(api, startid):
    tweet = "Test"
    for i in range(startid,startid+10):
        api.update_status(tweet+str(i))

def batch_tweet_from_file(api, filename):
    for line in reversed(open(filename).readlines()):
        api.update_status(line)


def compare(file1, file2):
    different = filecmp.cmp(file1, file2)
    return different


if __name__ == "__main__":
    username = "TestsssTom"

    cfg = get_credentials(username+".json")
    api = get_api(cfg)
    # desttroy all tweets on the page
    batch_delete(api)
    os.remove("TestingFiles/TestsssTom.txt")


    print "Deleted all Tweets"
    batch_tweet(api,0)
    print "First set of tweets printed"
    # get the tweets and match them with
    tweet_dumper.get_all_tweets5args(username, api, 3240, "TestingFiles/TestsssTom.txt", "lastTweetScraped.txt")
    firstPull = compare("TestingFiles/TestsssTom.txt", "TestingFiles/TestsssTomVerify1.txt")
    if not firstPull:
        print "scraped tweets do not match as expected"
    else:
        print "scraped tweets match desired output"

    # batch tweet 10 more
    batch_tweet(api,10)
    tweet_dumper.get_all_tweets5args(username, api, 3240, "TestingFiles/TestsssTom.txt", "lastTweetScraped.txt")
    fileappend = compare("TestingFiles/TestsssTom.txt", "TestingFiles/TestsssTomVerify2.txt")
    if not fileappend:
        print "appending new tweets not working"
    else:
        print "append tweets working"
    # delete all the tweets again
    batch_delete(api)


