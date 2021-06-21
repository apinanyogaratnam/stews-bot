emoji_list_text = [":pensive:", ":smile:"]
emoji_list_unicode = ["\U0001F614", "\U0001F601"]

# test on idle before deploying
def is_unicode_emoji(message):
    message = message.split()
    for word in message:
        if word in emoji_list_text:
            return True
    return False

def get_unicode_emoji(message):
    list_of_unicodes = []
    message = message.split()
    for word in message:
        if word in emoji_list_text:
            unicode = emoji_list_unicode[emoji_list_text.index(word)]
            list_of_unicodes.append(unicode)
    
    return list_of_unicodes