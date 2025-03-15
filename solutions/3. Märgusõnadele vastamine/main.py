response = get_response(message.content)  # Add in between these brackets the message that the bot received (look at task 2)
if response:
    await message.channel.send(response)  # Add the repsonse that we got from get_response()