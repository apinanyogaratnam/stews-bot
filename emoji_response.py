from emoji import UNICODE_EMOJI

def is_emoji(content):
    for emoji in UNICODE_EMOJI:
        if content == emoji:
            return True
    return False