import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "Ximk8dlrGGejLqL65TO39SqMD",
    "consumer_secret"     : "SiwVIoNUygs8FdZRAb4D3n6IdQUYPfUG82UNu2OwWUFhO9fq0l",
    "access_token"        : "705285627-hsGmup5zp84eZ6BPCqjmAWaR3g2YOXad3gPBnUac",
    "access_token_secret" : "Z6ws8O78em89H4ErpD5O2A0UM90t7hBXLxXRVH2Rson6V"
    }

  api = get_api(cfg)
  tweet = "SUPSUPSUP!!! #omgomg"
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()