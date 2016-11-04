
import tweepy #https://github.com/tweepy/tweepy
import re

def get_all_tweets(screen_name, api, amount):
    filename = "%s_tweets.txt" % screen_name
    get_all_tweets(screen_name, api, amount, filename)

def get_all_tweets(screen_name, api, amount, filename):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#initialize a list to hold all the tweepy Tweets
    alltweets = []
    
	# make request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200, include_rts = True)
    numTweets = len(new_tweets)
    # loop over first request and keep requesting until amount 
    # is reached or the 3240 threshold is reached
    while len(new_tweets) > 0:
        for tweet in new_tweets:
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
        oldest = new_tweets[-1].id - 1
        print "...%s tweets downloaded so far" % (len(alltweets))
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        if numTweets >= amount:
            break
        numTweets += len(new_tweets) 


    # write to txt file
    f = open(filename, 'w')
    # print len(alltweets)
    numbs = 0
    for tweet in alltweets:
        if tweet != "\n":
            f.write(tweet)
            f.write("\n")
        else:
            print tweet
        if numbs == 100:
            f.write("GRAB HER BY THE PUSSY! #MAGA\n")
            numbs = 0
        numbs += 1
    f.close()
