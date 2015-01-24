# Python + Twitter API = Love


## Creating a Twitter App

0. [Optional] Create a new Twitter account to post to (you could post to your own if you would like).
1. Login to your twitter account
2. Go to https://apps.twitter.com/ and click “Create New App”
3. Fill in the Data Twitter asks for (Name, Description, URL don’t matter for our purposes)
3a. Website must include the protocol (https://)
3b. Leave the callback url blank, we won’t need it for the Markov project
4. Agree to the Developer Agreement and Create the App
5. Click on the “Permissions” Tab and change the permissions to allow for Read & Write Access, save the form
6. Click on "Keys and Access Tokens”, Click on “Regenerate Consumer Key and Secret”, Confirm the action
7. Scroll to Access Tokens and click “Generate Access Token and Token Secret”

You now will have all of the Tokens / Consumer Keys you need.  You can now create a secrets.py file in your project folder and put the needed variables in there. I've included a snippet of the ones you'll want

````python
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
````



## File Reference
`markov.py` is the python file that does the tweeting

`.gitignore` is a handy dandy git feature that lets you check in a list of files that git should ignore and not ask you to commit.

`requirements.txt` is a helper file that I used to install the twitter-python library. You won't need it for the Markov project
