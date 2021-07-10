from imports import (discord, os, random, threading, 
                     time, keep_alive, contains_sad_words, 
                     contains_emoji, re, fetch_reddit_posts, 
                     NUMBER_OF_POSTS, ENCOURAGING_WORDS, 
                     THIRTY_MINUTES, HELP_MESSAGE, get_quote,
                     DAY)

# run auto push here
def push(time_to_sleep, filename):
    while True:
        email = os.environ['EMAIL']
        os.system('git config user.email "{}"'.format(email))
        os.system('touch Auto-Push/{}'.format(filename))
        os.system('python3 pygithub.py')
        time.sleep(time_to_sleep)
        os.system('rm Auto-Push/random.txt')
        os.system('python3 pygithub.py')
        time.sleep(time_to_sleep)


# fetching and appending reddit posts
all_subreddits = []

threading.Thread(target=fetch_reddit_posts, args=(THIRTY_MINUTES, NUMBER_OF_POSTS, all_subreddits)).start()
if False: threading.Thread(target=push, args=(DAY, "random.txt")).start()

client = discord.Client()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))


# @client.event
# async def on_member_join(member, message):
#     await message.channel.send(f'Hi {member.name}!, Welcome to our community!')
    # await member.create_dm()
    # await member.dm_channel.send(
    #     f'Hi {member.name}, welcome to my Discord server!'
    # )


@client.event
async def on_member_join(member):
    general_channel_id = 789004204777406464
    channel = client.get_channel(general_channel_id) # change to your channel id
    await channel.send(f"Welcome {member.mention}!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
    msg = message.content

    if msg.startswith("$birthday "):
        # adding a birthday to database
        import birthday_notifier
        date_string = msg[10:]
        if birthday_notifier.is_valid_format(date_string):
            birthday_notifier.add_birthday(message.author, date_string)
            await message.channel.send("Birthday of {} for {} added successfully.".format(date_string, message.author.display_name))
            from replit import db
            var = db[str(message.author)] # needs str() casting to be called
            await message.channel.send(var)
        else:
            await message.channel.send("Birthday Cannot be added due to invalid format.\n The format consists of: $birthday dd/mm/yyyy")


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
    
    # add (active message monitoring) into a new file and call function as active_monitoring(msg)
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

    # if message.content.startswith('LMFADODOASDOA'):
    #     # await message.channel.send('Clearing messages...')
    #     # async for msg in message.author.logs_from(message.channel):
    #     #       await message.delete()
    #     # await message.channel.send("Loading...")
    #     messages = await message.channel.history(limit=None).flatten() # extremely slow with limit=None
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
