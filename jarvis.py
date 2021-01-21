import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

print(voices[1].id)

engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    #speak("I am Jarvis, Sir! How may I assit Harshit? Shall I create a bong for Bhavik Bro?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please!")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourEmail@gmail.com', 'yourPasswordHere')
    server.sendmail('yourEmail@gmail.com', to, content)



if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia:")
            print(results)
            speak(results)

        if "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

            # C:\Pushpak\Apps\JARVIS\music
        elif "the box" in query:
            music_dir = "C:\Pushpak\Apps\JARVIS\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "box" in query:
            music_dir = "C:\Pushpak\Apps\JARVIS\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif "email to pushpak" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pushpaklive@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Pushpak, Mail send nahi hua.")

        elif "quit" in query:
            exit()

