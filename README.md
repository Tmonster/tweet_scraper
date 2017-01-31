# tweet_scraper
this project can be used to scrape tweets and append them to previously scraped tweets from the same user.
I built this so I could accumulate twitter data and train an RNN on it so it can post to twitter itself. 

The RNN I am using is also open source and can be found here https://github.com/jcjohnson/torch-rnn

Usage 

```
python getTweets.py screen_name amount [filename]
```

The filename is an optional argument to specify which file you want to write the tweets to
The filename can be used to append to files

The id of last tweet scraped is kept in a file called lastTweetScraped.txt which will be created if it does not exist in the current directory.

TODO's:

add specifity for arguments
-f file
-af append to file
-stop Scrape only new tweets, ie. all up to last tweet scraped as specified in the lastTweetScraped.txt file

Maybe scrape just a range
Better File I/O functionality
