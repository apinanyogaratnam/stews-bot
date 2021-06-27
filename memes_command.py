from imports import praw, os, time
from constants import MEME_SUBREDDITS
from dotenv import load_dotenv

# loading env variables
load_dotenv()


def createReddit():
   return praw.Reddit(client_id = os.environ.get['REDDIT_CLIENT_ID'],
                      client_secret = os.environ.get['REDDIT_CLIENT_SECRET'],
                      username = os.environ.get['REDDIT_USERNAME'],
                      password = os.environ.get['REDDIT_PASSWORD'],
                      user_agent = "stews_bot")


def fetch_subreddit_posts(subreddit_name, limit, reddit, all_subreddits):
    subreddit = reddit.subreddit(subreddit_name)
    top = subreddit.top(limit = limit)
  
    for post in top:
        all_subreddits.append(post)


def fetch_reddit_posts(delay, NUMBER_OF_POSTS, all_subreddits):
    while True:
        for meme_subreddit in MEME_SUBREDDITS:
            fetch_subreddit_posts(meme_subreddit, NUMBER_OF_POSTS, reddit, all_subreddits)

        time.sleep(delay)


reddit = createReddit()
