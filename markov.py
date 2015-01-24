import secrets
import twitter

def make_text():
    return "Some Hardcoded string"

api = twitter.Api(
    consumer_key=secrets.TWITTER_CONSUMER_KEY,
    consumer_secret=secrets.TWITTER_CONSUMER_SECRET,
    access_token_key=secrets.TWITTER_ACCESS_TOKEN,
    access_token_secret=secrets.TWITTER_ACCESS_TOKEN_SECRET
)


status = api.PostUpdate(make_text)
