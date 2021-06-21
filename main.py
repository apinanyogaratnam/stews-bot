from imports import (discord, praw, os, random, threading, time,requests, json, keep_alive, contains_sad_words, contains_emoji, re)

encouraging_words = [
  "aw man hope you feel better >.<",
  "It's ok everything will get better",
  "Whatever you're going through, you got this!",
  "Keep fighting!",
  "Stay strong",
  "Never give up"
]

reddit = praw.Reddit(client_id = os.environ['REDDIT_CLIENT_ID'],
                          client_secret = os.environ['REDDIT_CLIENT_SECRET'],
                          username = os.environ['REDDIT_USERNAME'],
                          password = os.environ['REDDIT_PASSWORD'],
                          user_agent = "stews_bot")

NUMBER_OF_POSTS = 50

# fetching and appending reddit posts
all_subreddits = []

def fetch_subreddit_posts(subreddit_name, limit):
    subreddit = reddit.subreddit(subreddit_name)
    top = subreddit.top(limit = limit)
  
    for post in top:
        all_subreddits.append(post)


def fetch_reddit_posts(delay):
    fetch_subreddit_posts("memes", NUMBER_OF_POSTS)
    fetch_subreddit_posts("Memes_Of_The_Dank", NUMBER_OF_POSTS)
    fetch_subreddit_posts("memes", NUMBER_OF_POSTS)
    fetch_subreddit_posts("dankmemes", NUMBER_OF_POSTS)

    time.sleep(delay)

thirty_minutes = 60*30
threading.Thread(target=fetch_reddit_posts, args=(thirty_minutes,)).start()
fetch_reddit_posts(0)

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']

  print(quote)
  if (("Obtain an auth key for unlimited") in quote):
    quote = "It is better to fail in originality than to succeed in imitation. -Herman Melville"
    return quote

  return (quote)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))


@client.event
async def on_member_join(member):
    await message.channel.send(f'Hi {member.name}!, Welcome to our community!')
    # await member.create_dm()
    # await member.dm_channel.send(
    #     f'Hi {member.name}, welcome to my Discord server!'
    # )


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if message.content.startswith('$hello'):
    await message.channel.send(f'Hello {message.author.display_name}!')

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  if contains_sad_words(msg) and not contains_emoji(msg):
      await message.channel.send(random.choice(encouraging_words))
  
  if msg.startswith('$help'):
    await message.channel.send(
      "Here are the different commands available:\n" + 
      "$hello (says hello)\n" + 
      "$inspire (says an inspirational message)\n" + 
      "$meme (gives a meme from reddit subreddit memes, discresion is advised)\n" +
      "Here are the different keywords:\n" + 
      "kms, down bad, depressed, sad (gives a positive message)"
    )

  if msg.startswith('$meme'):
      random_sub = random.choice(all_subreddits)

      name = random_sub.title
      url = random_sub.url
      embed = discord.Embed(title = name)
      
      embed.set_image(url = url)
      await message.channel.send(embed = embed)

  if msg.startswith('pls shirt'):
      await message.channel.send("ilya shirt coming soon)")
  
  custom_emojis = re.findall(r'<:\w*:\d*>', msg)
  print(custom_emojis)
  for emoji in custom_emojis:
      await message.add_reaction(emoji='/'+emoji)

  for mention in message.mentions:
      if mention.name == "Stews Bot":
          await message.channel.send("who called me?")
          time.sleep(2)
          await message.channel.send(f'oh hey {message.author.display_name}!')

keep_alive()

my_secret = os.environ['TOKEN']
client.run(my_secret)
