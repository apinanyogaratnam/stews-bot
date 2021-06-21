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
from inspire_command import contains_sad_words, contains_emoji
