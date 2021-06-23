from imports import praw, os, time
from constants import MEME_SUBREDDITS


def createReddit():
   return praw.Reddit(client_id = os.environ['REDDIT_CLIENT_ID'],
                      client_secret = os.environ['REDDIT_CLIENT_SECRET'],
                      username = os.environ['REDDIT_USERNAME'],
                      password = os.environ['REDDIT_PASSWORD'],
                      user_agent = "stews_bot")


def fetch_subreddit_posts(subreddit_name, limit, reddit, all_subreddits):
    subreddit = reddit.subreddit(subreddit_name)
    top = subreddit.top(limit = limit)
  
    for post in top:
        all_subreddits.append(post)


def fetch_reddit_posts(delay, NUMBER_OF_POSTS, all_subreddits):
    for meme_subreddit in MEME_SUBREDDITS:
        fetch_subreddit_posts(meme_subreddit, NUMBER_OF_POSTS, reddit, all_subreddits)
    fetch_subreddit_posts("memes", NUMBER_OF_POSTS, reddit, all_subreddits)
    fetch_subreddit_posts("Memes_Of_The_Dank", NUMBER_OF_POSTS, reddit, all_subreddits)
    fetch_subreddit_posts("memes", NUMBER_OF_POSTS, reddit, all_subreddits)
    fetch_subreddit_posts("dankmemes", NUMBER_OF_POSTS, reddit, all_subreddits)
    fetch_subreddit_posts("MemesIRL", NUMBER_OF_POSTS, reddit, all_subreddits)

    time.sleep(delay)


reddit = createReddit()
