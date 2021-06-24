from imports import (discord, os, random, threading, 
                     time, requests, json, keep_alive,
                     contains_sad_words, contains_emoji, 
                     re, fetch_reddit_posts, NUMBER_OF_POSTS,
                     ENCOURAGING_WORDS, THIRTY_MINUTES, 
                     HELP_MESSAGE)


# fetching and appending reddit posts
all_subreddits = []

threading.Thread(target=fetch_reddit_posts, args=(THIRTY_MINUTES,NUMBER_OF_POSTS, all_subreddits)).start()
# fetch_reddit_posts(0, NUMBER_OF_POSTS, all_subreddits)

client = discord.Client()

# put this in inspire command file
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']

  print(quote)
  if (("Obtain an auth key for unlimited") in quote):
    quote = "It is better to fail in originality than to succeed in imitation. -Herman Melville"
    return quote

  return quote


@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))


@client.event
async def on_member_join(member, message):
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
        await message.channel.send(random.choice(ENCOURAGING_WORDS))
    
    if msg.startswith('$help'):
        await message.channel.send(HELP_MESSAGE)

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
    for emoji in custom_emojis:
        try:
            await message.add_reaction(emoji='/'+emoji)
        except:
          print("- emoji from different server")

    for mention in message.mentions:
        if mention.name == "Stews Bot":
            await message.channel.send("who called me?")
            time.sleep(2)
            await message.channel.send(f'oh hey {message.author.display_name}!')

    if "\U0001F614" in message.content:
        await message.add_reaction(emoji="\U0001F614")

    # if message.content.startswith('!clear -ls -now'):
    #     # await message.channel.send('Clearing messages...')
    #     # async for msg in message.author.logs_from(message.channel):
    #     #       await message.delete()
    #     # await message.channel.send("Loading...")
    #     messages = await message.channel.history(limit=500).flatten() # extremely slow with limit=None
    #     print(len(messages))
    #     for text_msg in messages:
    #         if text_msg.author.name == message.author.name:
    #             await text_msg.delete()
    #     await message.channel.send("\U0001F44D")

    # make a delete bot history everywhere including removing reactions
    # if message.content.startswith("!clear stews bot"):
    #     await message.channel.send('clearing messages...')
    #     messages = await message.channel.history().flatten()
    #     for text_msg in messages:
    #         if text_msg.author.name == "Stews Bot":
    #             await text_msg.delete()

    # if message.content.startswith("$spam"):
keep_alive()

my_secret = os.environ['TOKEN']
client.run(my_secret)
