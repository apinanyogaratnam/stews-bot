import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

sad_words = ["kms", "down bad", "depressed", "sad"]
encouraging_words = [
  "aw man hope you feel better >.<",
  "It's ok everything will get better",
  "Whatever you're going through, you got this!"
]

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
    await message.channel.send("Hello!")

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  if any((word in msg) for word in sad_words):
    if "willsad" not in msg and "sadge" not in msg.lower():
      await message.channel.send(random.choice(encouraging_words))
  
  if msg.startswith('$help'):
    await message.channel.send(
      "Here are the different commands available:\n" + 
      "$hello (says hello)\n" + 
      "$inspire (says an inspirational message)\n" + 
      "Here are the different keywords:\n" + 
      "kms, down bad, depressed, sad (gives a positive message)"
    )

keep_alive()

my_secret = os.environ['TOKEN']
client.run(my_secret)
