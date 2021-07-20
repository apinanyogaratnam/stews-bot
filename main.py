from imports import (discord, os, random, threading, 
                     time, keep_alive, contains_sad_words, 
                     contains_emoji, re, fetch_reddit_posts, 
                     NUMBER_OF_POSTS, ENCOURAGING_WORDS, 
                     THIRTY_MINUTES, HELP_MESSAGE, get_quote,
                     DAY, push)
from birthday_notifier import is_anyones_birthday
from MessageTriggerCommands.command_functions import commands
commit_to_gh = True

# fetching and appending reddit posts
all_subreddits = []

threading.Thread(target=fetch_reddit_posts, args=(THIRTY_MINUTES, NUMBER_OF_POSTS, all_subreddits)).start()
if commit_to_gh: threading.Thread(target=push, args=(DAY, "random.txt")).start()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))


async def check_for_birthdays(time_to_sleep):
    while True:
        import datetime
        now = datetime.datetime.now()

        if not now.hour == (9 + 4): 
            time.sleep(time_to_sleep)
            continue

        lst_of_users_today = is_anyones_birthday()
        channel = client.get_channel(836106300596944896)

        for cord_user_id in lst_of_users_today:
            await channel.send("Hey Everyone, Let's wish <@" + cord_user_id + "> Happy Birthday!!!")
            
        time.sleep(time_to_sleep)


import asyncio
threading.Thread(target=asyncio.run, args=(check_for_birthdays(THIRTY_MINUTES*2),)).start()


@client.event
async def on_member_join(member):
    server_id = 750477536353583205
    general_channel_id = 789004204777406464
    guild = client.get_guild(server_id)
    channel = guild.get_channel(general_channel_id)

    await channel.send(f"Hey {member.mention}, Welcome to {guild.name}! :partying_face:")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
    msg = message.content

    # change to in
    # if msg.lower() in " sadge ":
    #     await message.channel.send(":sadge:")
    if (message.content == ("api")):
        voiceChannel = discord.utils.get(client.guild.voice_channels, name="vc-general")
        voice = discord.utils.get(client.voice_clients, guild=client.guild)
        if not voice.is_connected():
            await voiceChannel.connect()


    if (str(message.author) == "vai9er#5526"):
        await message.channel.send("-play grubhub delivery dance")

    if msg.startswith("$birthday "):
        # adding a birthday to database
        import birthday_notifier
        date_string = msg[10:]
        if birthday_notifier.is_valid_format(date_string):
            confirmation_message = birthday_notifier.add_birthday(message.author.id, date_string)
            await message.channel.send(confirmation_message)

        else:
            await message.channel.send("Birthday Cannot be added due to invalid format.\n The format consists of: $birthday dd/mm/yyyy")


    await commands.hello_command(message)
    await commands.inspire_command(message)
    await commands.help_command(message)
    await commands.meme_command(message, all_subreddits)
    await commands.shirt_command(message)
    await commands.programming_excuses_command(message)

    if contains_sad_words(msg) and not contains_emoji(msg):
        await message.channel.send(random.choice(ENCOURAGING_WORDS))

    if msg.startswith('$q: '):
        await message.channel.send("It's currently inactive. Ask stews (stewietheangel#6223) to turn on the command")
    
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
            break

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
