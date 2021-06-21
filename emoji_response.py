from emoji import UNICODE_EMOJI

def is_emoji(content):
    content = content[1:-2]
    for emoji in UNICODE_EMOJI:
        if content == emoji:
            return True
    return False