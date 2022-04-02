import gtts
from playsound import playsound
from jokeapi import Jokes # Import the Jokes class
import asyncio
async def print_joke():
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke(blacklist=['nsfw','racist','sexist','religious','political','explicit'])  # Retrieve a random joke
    if joke["type"] == "single": # Print the joke
        print(joke["joke"])
        tts = gtts.gTTS(joke["joke"],lang="en")
        tts.save("joke.mp3")
        playsound("joke.mp3")
    else:
        print(joke["setup"])
        print(joke["delivery"])
        tts = gtts.gTTS(joke["setup"]+" " + joke["delivery"],lang="en")
        tts.save("joke.mp3")
        playsound("joke.mp3")

asyncio.run(print_joke())
