from random import randint
"""
TODO 3.2: Add here the message that will be read from discord and response to that message

For example, the bot receives the message "hello", then we want to reply to that "Hello there!"
For that we would need to add to the responses dictionary the following line
    "hello": "Hello there!",         # First string is command, second one is response
"""
responses = {
    "": "",
}

"""
TODO 3.3: Get the response in the responses dictionary.
"""
def get_response(user_input: str) -> str:
    user_input: str = user_input.lower()
    if user_input == "roll dice":  # if the input is roll_dice, then return the random number that was found with the dice roll
        return roll_dice()
    else:
        return responses.get()  # TODO: Add user_input in between the brackets, this way we get the response by inputting our command


"""
TODO 3.4: Add a correct range for dice rolling
"""
def roll_dice():
    return str(randint(0, 0))  # The randint function will return a random integer in between the two numbers
