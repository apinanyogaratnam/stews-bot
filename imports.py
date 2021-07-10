# standard libary imports
import os
import random
import threading
from threading import Thread
import time
import re
import requests
import json

# Third party imports
import discord
import praw
from flask import Flask

# local file imports
from keep_alive import keep_alive
from inspire_command import get_quote
from memes_command import createReddit, reddit, fetch_reddit_posts
from constants import (NUMBER_OF_POSTS, ENCOURAGING_WORDS, THIRTY_MINUTES,
                       MEME_SUBREDDITS, HELP_MESSAGE, DAY)
from inspire_command import contains_sad_words, contains_emoji
from AutoPush.push_to_github import push
