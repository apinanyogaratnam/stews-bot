async def hello_command(message):
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello {message.author.display_name}!')
