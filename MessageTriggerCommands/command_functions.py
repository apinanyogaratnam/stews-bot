from imports import (get_quote, HELP_MESSAGE, random, discord)

class commands:
    async def hello_command(message):
        # might remove if statement
        if message.content.startswith('$hello'):
            await message.channel.send(f'Hello {message.author.display_name}!')


    async def inspire_command(message):
        # might remove if statement
        if message.content.startswith('$inspire'):
                quote = get_quote()
                await message.channel.send(quote)


    async def help_command(message):
        if message.content.startswith('$help'):
            await message.channel.send(HELP_MESSAGE)


    async def meme_command(message, all_subreddits):
        if message.content.startswith('$meme'):
                random_sub = random.choice(all_subreddits)

                name = random_sub.title
                url = random_sub.url
                embed = discord.Embed(title = name)

                embed.set_image(url = url)
                await message.channel.send(embed = embed)


    async def shirt_command(message):
        if message.content.startswith('pls shirt'):
            await message.channel.send("ilya shirt coming soon)")
