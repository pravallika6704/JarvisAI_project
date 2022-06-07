# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyttsx3
import speech_recognition as sr
from speech_recognition import Recognizer
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 170)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

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