import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def get_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"User said: {command}")
    except Exception as e:
        print("Sorry, I didn't catch that. Please try again.")
        command = None

    return command

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    command = get_command()

    if command is None:
        continue

    if "set a reminder" in command:
        # Code to set a reminder
        speak("Reminder set.")
    elif "create a to-do list" in command:
        # Code to create a to-do list
        speak("To-do list created.")
    elif "search the web" in command:
        # Code to search the web
        speak("Searching the web.")
    elif "exit" in command:
        speak("Goodbye!")
        break
    else:
        speak("Sorry, I didn't understand your command. Please try again.")

