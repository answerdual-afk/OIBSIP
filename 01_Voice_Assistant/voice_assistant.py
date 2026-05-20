import pyttsx3
import datetime
import webbrowser

# Function to speak
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Startup
speak("Hello, I am your voice assistant")

while True:
    command = input("Enter your command: ").lower()

    if "hello" in command:
        speak("Hello, how are you")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    
    elif "spotify" in command:
        webbrowser.open("https://spotify.com")
        speak("Opening Spotify")

    elif "joke" in command:
        speak("Why do programmers prefer dark mode? Because light attracts bugs. hahahaha")

    elif "bye" in command:
        speak("Goodbye")
        break

    else:
        speak("Sorry, I did not understand")
