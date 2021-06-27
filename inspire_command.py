import random, json, requests
from quotes_inventory import get_quotes
sad_words = ["kms", "down bad", "depressed", "sad"]

encouraging_words = [
  "aw man hope you feel better >.<",
  "It's ok everything will get better",
  "Whatever you're going through, you got this!"
]


def contains_sad_words(message):
    if any((word in message.split()) for word in sad_words):
        return True

    return False


def contains_emoji(message):
    if (message.count(":") >= 2):
        return True

    return False

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']

  print(quote)
  if (("Obtain an auth key for unlimited") in quote):
      quote = random.choice(get_quotes())
      
      return quote

  return quote

