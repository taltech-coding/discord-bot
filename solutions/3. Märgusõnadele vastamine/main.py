@client.event
async def on_message(message: Message):
    if message.content.startswith("?"):
        await client.process_commands(message)
        return

    response = get_response(message.content)
    if response:
        await message.channel.send(response)