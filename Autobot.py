from click import command
import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes
import webbrowser



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Command Recognition
def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Please wait...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(e)
        speak("Please Repeat")
        query="none"
    return query

# Greetings
def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Boss                    How can I help You!")
        speak("Good Morning Boss                    How can I help You!")
    elif hour>=12 and hour<17:
        print("Good Afternoon Boss                  How can I help You!")
        speak("Good Afternoon Boss                  How can I help You!")
    elif hour>=17 and hour<21:
        print("Good Evening Boss                    How can I help You!")
        speak("Good Evening Boss                    How can I help You!")
    else:
        print("Good Night Boss                      How can I help You!")
        speak("Good Night Boss                      How can I help You!")


#time speak
if __name__ == "__main__":
    wishings()
    while True:
        query = commands().lower()
        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        #open any application
        elif 'open chrome' in query:
            speak("Opening Chrome")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'open visual studio' in query:
            speak("Opening VSCode")
            os.startfile("C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
        # open website
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")
        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in")
            speak("opening google")
        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("opening youtube")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("opening whatsapp")
        elif 'cartoon' in query:
            webbrowser.open("https://aniwatch.to/home?source=pwa")
            speak("opening aniwatch")
        
        #search information from wikipedia
        elif 'wikipedia' in query:
            speak("Searching Wikipedia")
            try:
                query=query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=10)
                speak("According to Wikipedia,")
                print(results)
                speak(results)
            except:
                speak("No result found")
                print("No reult found")

        #Voice Change
        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        #Volume Increase and Decrease
        elif ("volume up" in query) or ("increase volume" in query):
            pyautogui.press("volumeup")
            speak('volume increased')
        elif ("volume down" in query) or ("decrease volume" in query):
            pyautogui.press("volumedown")
            speak('volume decreased')

        #Names
        elif 'Creator' in query:
            speak("I was Created by Narayan")
            print("I was Created by Narayan")
        elif 'your name' in query:
            speak("My name is AutoBot")
            print("My name is AutoBot")

        #play music
        elif 'play music' in query:
            speak("Here you go with Music")
            music_dir = "C:\\Users\\DELL\\OneDrive\\Desktop\\AutoBot\\music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[0]))

        # Send a WhatsApp Message to a Contact at HH:MM(24hourstime)
        elif 'whatsapp' in query:
            pywhatkit.sendwhatmsg("+917588428967", "Hi I am AutoBot", 18, 31)

        #Play on youtube
        elif 'play' in query:
            query=query.replace('play', '')
            speak('Playing' + query)
            pywhatkit.playonyt(query)

        #Names
        elif 'creator' in query:
            speak("My creator name is Narayan")
        elif 'your name' in query:
            speak("My name is AutoBot")

        #type on available app
        elif 'type' in query:
            speak("Tell me what to write")
            while True:
                writeInNotepad=commands()
                if writeInNotepad=='exit typing':
                    speak("Writing completed")
                else:
                    pyautogui.write(writeInNotepad)

        #tell a joke
        elif 'joke' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)
            
        #exit terminal
        elif 'shutdown' in query:
            speak("Okay Boss, See you soon")
            quit()


