sad_words = ["kms", "down bad", "depressed", "sad"]

encouraging_words = [
  "aw man hope you feel better >.<",
  "It's ok everything will get better",
  "Whatever you're going through, you got this!"
]


def contains_sad_words(message):
  if any((word in message) for word in sad_words):
      return True


def contains_emoji(message):
  if (message.count(":") >= 2):
    return True