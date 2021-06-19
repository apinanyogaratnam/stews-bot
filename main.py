import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

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
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(encouraging_words))
  
  if msg.startswith('$help'):
    await message.channel.send()

keep_alive()
client.run(my_secret)
