import pyttsx3
import speech_recognition as sr
from speech_recognition import Recognizer



Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')

Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 170)


def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f"A.I : {audio}")
    print("   ")
    Assistant.runAndWait()


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        command.pause_threshold = 1
        audio = command.listen(source, 0, 2)

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio, language='en-in')
            print(f"You said : {query}")

        except Exception as Error:
            return None

        query = str(query)
        return query.lower()



def TaskExe():
    while True:
        query=takecommand()
        if 'hello' in query:
            Speak("Hello Sir, I am Jarvis")
            Speak("Your Personal AI Assistant!")
            Speak("How may I help you")

        elif 'how are you' in query:
            Speak("I am fine Sir!")

TaskExe()