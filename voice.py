import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    speak("Hello! How can I help you today?")

# Function to recognize user's voice command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-us')
        print("User:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Can you please repeat?")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

# Function to handle user queries
def handle_query(query):
    if "hello" in query:
        speak("Hi there!")
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in query:
        speak("What do you want me to search for?")
        search_query = listen()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")
    elif "exit" in query:
        speak("exit")
        exit()
    else:
        speak("Sorry, I couldn't understand that.")

# Main function to run the voice assistant
def main():
    greet()
    while True:
        query = listen()
        if query:
            handle_query(query)

if __name__ == "__main__":
    main()
