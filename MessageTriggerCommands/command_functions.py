from imports import get_quote

async def hello_command(message):
    # might remove if statement
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello {message.author.display_name}!')


async def inspire_command(message):
    # might remove if statement
    if message.content.startswith('$inspire'):
            quote = get_quote()
            await message.channel.send(quote)
