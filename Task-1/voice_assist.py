import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Adjust sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1.0)
        print("\nListening... Please speak clearly.")
        try:
            # Set longer timeout and phrase time limit
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=5)
            print("Processing your command...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            speak("I didn't catch that. Please try again.")
            print("Timeout: No input detected.")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that. Can you repeat?")
            print("Error: Unable to recognize speech.")
        except sr.RequestError as e:
            speak(f"Could not request results; {e}")
            print(f"Request Error: {e}")
    return ""

def get_time():
    """Get the current time."""
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date():
    """Get the current date."""
    today = datetime.datetime.now()
    return today.strftime("%A, %B %d, %Y")

def search_web(query):
    """Search the web using the query."""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the results for {query} on the web.")
    print(f"\nSearch results for {query} are displayed on your browser.\n")

def process_command(command):
    """Process the voice command and take appropriate action."""
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = get_time()
        speak(f"The current time is {current_time}.")
        print(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = get_date()
        speak(f"Today's date is {current_date}.")
        print(f"Today's date is {current_date}.")
    elif "search" in command:
        speak("What do you want me to search for?")
        query = listen()
        if query:
            search_web(query)
            return True
    elif "stop" in command or "exit" in command:
        speak("Goodbye! and thank you for using me.")
        return False
    else: 
        speak(f"You said: {command}. But I am not programmed for that yet.")
        speak("I can assist you with current time, date, and web browsing.")
        speak("You may speak now.")
    return True

def main():
    """Main function to run the voice assistant."""
    speak("Welcome! I am your voice assistant.")
    speak("You can ask for the current time, date, or use the search command to Google anything.")
    speak("You may speak now.")
    active = True
    while active:
        command = listen()
        if command:
            active = process_command(command)

if __name__ == "__main__":
    main()
