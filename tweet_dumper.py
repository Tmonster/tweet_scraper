import tweepy #https://github.com/tweepy/tweepy
import sys
import os
import re

def updateLastTweet(filename, screen_name, newLastTweet):
    tmpLine = ""
    newData = ""
    if not os.path.isfile(filename):
        newFile = open(filename, 'w')
        newFile.close()
    with open(filename, 'r+b') as f:
        for line in f:
            tmpLine = line.split(':')
            if tmpLine[0] == screen_name:
                newData += tmpLine[0] + ":" + str(newLastTweet) +  "\n"
            else:
                newData += line
    newF = open(filename + ".swp", 'w')
    newF.write(newData)
    newF.close()
    os.remove(filename)
    os.rename(filename + ".swp", filename)

def getMostRecentTweet(filename, screen_name):
    if not os.path.isfile(filename):
        newFile = open(filename, 'w')
        newFile.close()
    with open(filename, 'r+b') as f:
        for line in f:
            tmpLine = line.split(":")
            if tmpLine[0] == screen_name:
                MostRecentTweetPulled = tmpLine[1].strip()
                f.close()
                return MostRecentTweetPulled
    f = open(filename, 'a')
    newEntry = screen_name + ":0"
    f.write(newEntry)
    f.close()
    return 0

def get_all_tweets3args(screen_name, api, amount):
    filename = "%s_tweets.txt" % screen_name
    lastTweetId = "lastTweetScraped.txt"
    get_all_tweets5args(screen_name, api, amount, filename, lastTweetId)

def get_all_tweets4args(screen_name, api, amount, filename):
    lastTweetId = "lastTweetScraped.txt"
    get_all_tweets5args(screen_name, api, amount, filename, lastTweetId)


def writeTweets(filename, mode, tweets):
    f = open(filename, mode)
    # print len(alltweets)
    for tweet in tweets:
        if tweet != "\n" or tweet != "":
            f.write(tweet)
            f.write("\n")
    f.close()

def get_all_tweets5args(screen_name, api, amount, filename, lastTweetScrapedFile):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200, include_rts = True)
    numTweets = len(new_tweets)
    MostRecentTweetPulled = getMostRecentTweet(lastTweetScrapedFile, screen_name)
    print "Most Recent Tweet Pulled =", MostRecentTweetPulled

    # record most recent tweet id.
    # The id of the last tweet the user tweeted.
    if len(new_tweets) > 0:
        most_recent_tweet = new_tweets[0].id
    else:
        most_recent_tweet = 0
    # loop over first request and keep requesting until amount
    # is reached or the 3240 threshold is reached
    while len(new_tweets) > 0:
        for tweet in new_tweets:
            if int(MostRecentTweetPulled) >= int(tweet.id):
                print "Most Recent Tweet Pulled =", MostRecentTweetPulled
                print "tweet.id = ", tweet.id
                numTweets = amount
                break
            try:
                tweet = tweet.text.decode('string_escape', 'ignore').encode('ascii', 'ignore')
            except UnicodeEncodeError:
                strippedTweet = ""
                for character in tweet.text:
                    if ord(character) > 126 or ord(character) < 32:
                        continue
                    else:
                        strippedTweet+=character
                tweet = strippedTweet
            # strip URLS, Ampersands, retweets, and newlines
            tweet = re.sub(r'(?:www|https?)[^\s]+', '', tweet, flags=re.MULTILINE)
            tweet = re.sub(r'&amp;', '&', tweet, flags=re.MULTILINE)
            tweet = re.sub(r'^RT.*:+ ', '', tweet, flags=re.MULTILINE)
            tweet = tweet.replace('\n', ' ')
            tweet = tweet.strip()
            alltweets.append(tweet)
            if len(alltweets) >= amount:
                numTweets = len(alltweets)
                break
        oldest = new_tweets[-1].id - 1
        print "...%s tweets downloaded so far" % (len(alltweets))
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        if numTweets >= amount:
            break
        numTweets += len(new_tweets)

    writeTweets(filename, 'a', alltweets)
    # write to txt file
    updateLastTweet(lastTweetScrapedFile, screen_name, most_recent_tweet)


