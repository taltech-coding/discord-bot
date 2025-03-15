if message.content.startswith("?"):
    await client.process_commands(message)
    return