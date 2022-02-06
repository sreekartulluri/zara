import webbrowser
import pyfiglet
import requests
from bs4 import BeautifulSoup
import serial
import datetime
import pyaudio
import requests
import time
import wikipedia
import pyjokes
import pyautogui
import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
pyfiglet.print_figlet("ZARA")
def speaktext(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',180)
    engine.say(command)
    engine.runAndWait()

while 1:
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2)
            audio2 = r.listen(source2)
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say " + MyText)

            result = wikipedia.search(MyText)

            if 'play music' in MyText:
                speaktext("ok boss")
                speaktext("what song do you want me to play")
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                speaktext("playing" + MyText)
                result = webbrowser.open("https://www.youtube.com/")

            if "zara" in MyText:
                speaktext("yes boss")
            if "sara" in MyText:
                speaktext("yes boss")

            if "keep me updated on tech" in MyText:
                speaktext("sure boss, on it ")
                webbrowser.open("https://gadgets.ndtv.com/news")

            if "hello" in MyText:
                 speaktext("hello boss i am your voice assistant")
                 speaktext("do you need anything???")

            if "what is the date today" in MyText:
                speaktext(datetime.date.today())

            if "what's the time" in MyText:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                speaktext(current_time)
            if "what is the time" in MyText:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                speaktext(current_time)
            if "what is the time now " in MyText:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                speaktext(current_time)
            if "what is your name" in MyText:
                speaktext("my name is zaara")
                speaktext("i am your personal voice assistant")
            if "who are you" in MyText:
                speaktext("my name is zaara")
                speaktext("i am your personal voice assistant")
            if 'what can you do' in MyText:
                    speaktext(" i can open apps, search web and assist you ")

            if 'tell me about yourself' in MyText:
                speaktext("i am a personal voice assistant to you")
                speaktext("i am programmed in python by sreekar")

            if 'open chrome' in MyText:
                speaktext("opening google chrome")
                webbrowser.open("www.google.com")

            if "open spotify" in MyText:
             speaktext("opening spotify")
             webbrowser.open("https://open.spotify.com/?nd=1")

            if "code blue" in MyText:
                speaktext("initiating code blue boss")
                webbrowser.open("https://gadgets.ndtv.com/finance/crypto-currency-price-in-india-inr-compare-bitcoin-ether-dogecoin-ripple-litecoin")
                webbrowser.open("https://coindcx.com/portfolio")

            if "i am bored" in MyText:
                speaktext("dont worry boss")
                speaktext("ill play your favorite playlist now")
                webbrowser.open("https://open.spotify.com/playlist/4v5EPfDF5Ch3PzMMAyFgxP")

            if "volume up" in MyText:
                pyautogui.press("volumeup")

            if "volume down" in MyText:
                pyautogui.press("volumedown")

            if "mute" in MyText:
                pyautogui.press("volumemute")

            if "open whatsapp" in MyText:
                speaktext("opening whatsapp now")
                webbrowser.open("https://web.whatsapp.com/")

            if "open github" in MyText:
                speaktext("opening your github page")
                webbrowser.open("https://github.com/sreekartulluri")

            if "tell me a joke" in MyText:
                speaktext("sure boss")
                speaktext(pyjokes.get_joke(language='en',category='all'))

            if "wikipedia" in MyText:
                speaktext("what meaning do you want boss")
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                result = wikipedia.search(MyText)
                speaktext("searching wikipedia")
                speaktext(wikipedia.page(MyText).summary)
            continue
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
     print("noice")
