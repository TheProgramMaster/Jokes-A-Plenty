import tkinter as tk
import time
from xml.etree.ElementTree import TreeBuilder
import gtts
from playsound import playsound
from jokeapi import Jokes # Import the Jokes class
import asyncio
import random
from flask import Flask, redirect, url_for
languages = list(gtts.lang.tts_langs().keys())
def quit_screen():
    quit()
def contact_button():
    contactWindow = JokesAPlentyContactScreen()
    quit()
async def print_joke():
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke(blacklist=['nsfw','racist','sexist','religious','political','explicit'])  # Retrieve a random joke
    blah = input("would you like to hear the joke in a random language's accent or a normal American accent? (random or american): ")
    if blah == "random":
        if joke["type"] == "single": # Print the joke
            temp = joke["joke"]
            print(temp)
            tts = gtts.gTTS(temp,lang=random.choice(languages))
            tts.save("joke.mp3")
            playsound("joke.mp3")
            #return joke["joke"]
        else:
            temp = joke["setup"]
            print(temp)
            tts = gtts.gTTS(temp,lang=random.choice(languages))
            tts.save("joke.mp3")
            playsound("joke.mp3")
            temp = joke["delivery"]
            print(tempTwo)
            tts = gtts.gTTS(tempTwo,lang=random.choice(languages))
            tts.save("jokeTwo.mp3")
            playsound("jokeTwo.mp3")
            #return joke["setup"] + joke["delivery"]
    else:
        if joke["type"] == "single": # Print the joke
            temp = joke["joke"]
            print(temp)
            tts = gtts.gTTS(temp,lang="en")
            tts.save("joke.mp3")
            playsound("joke.mp3")
            return joke["joke"]
        else:
            temp = joke["setup"]
            print(temp)
            tts = gtts.gTTS(temp,lang="en")
            tts.save("joke.mp3")
            playsound("joke.mp3")
            tempTwo = joke["delivery"]
            print(tempTwo)
            tts = gtts.gTTS(tempTwo,lang="en")
            tts.save("jokeTwo.mp3")
            playsound("jokeTwo.mp3")
            return joke["setup"] + joke["delivery"]
def runJoke():
    asyncio.run(print_joke())
window = tk.Tk()
window.title("Jokes A Plenty")
window.geometry("1000x1000")
titleLabel = tk.Label(text="Jokes-A-Plenty")
titleLabel.pack()
titleLabel.place(x=500,y=0)
description = tk.Label(text="Hello there! Welcome to Jokes " +
                       "A Plenty! This is a Python-Powered program that will be"
                       + " sure to put a laugh on your face at the end of the day!")
description.pack()
description.place(x=0,y=50)
descriptionTwo = tk.Label(text="Using the JokeAPI, our program processes numerous " +
                          "jokes at random and tells them to you in the form of a robot.")
descriptionTwo.pack()
descriptionTwo.place(x=0,y=100)
descriptionThree = tk.Label(text="We also provide these jokes to you not only with their content at random, " +
                          "but the accents utilized at random, as well. We hope this will make your day " +
                          "a little but brighter, and your mood a tad more light. Enjoy!")
descriptionThree.pack()
descriptionThree.place(x=0,y=150)
descriptionQuit = tk.Label(text="Be sure to click the \'Quit\' button below to quit this program.")
descriptionQuit.pack()
descriptionQuit.place(x=0,y=200)
quitButton = tk.Button(text="Quit",command=quit_screen)
quitButton.pack()
quitButton.place(x=500,y=250)
jokeButton = tk.Button(text="Joke",command=runJoke)
jokeButton.pack()
jokeButton.place(x=500,y=300)
window.mainloop()
