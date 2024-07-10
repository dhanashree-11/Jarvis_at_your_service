import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
# Assuming musicLibrary is a custom module you have created.
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "use your api key"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, I can't find that song in the music library.")
    elif "news" in c.lower():
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()
    
            # Extract and print the headlines
            headlines = data.get('articles', [])
            for i, article in enumerate(headlines):
                speak(f"{i+1}. {article['title']}")
        else:
            speak(f"Failed to fetch news: {response.status_code}")
    elif "stop" in c.lower() or "exit" in c.lower() or "quit" in c.lower():
        speak("Goodbye!")
        return False
    
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for the wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)
                if "jarvis" in word.lower():
                    speak("Yes?")
                    print("Jarvis Active ...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print(f"Command received: {command}")
                    processCommand(command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
