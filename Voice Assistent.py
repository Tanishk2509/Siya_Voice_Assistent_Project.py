import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize speech
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for the wake word 'Hello Bro'...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise

        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)  # Listen with timeouts
            print("Recognizing...")

            try:
                # Recognize speech and convert it to text
                command = recognizer.recognize_google(audio).lower()
                print(f"Command received: {command}")
                
                return command
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                return None
            except sr.RequestError as e:
                print(f"Error with the service: {e}")
                return None
        except sr.WaitTimeoutError:
            print("No speech detected, please try again.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

# Function to process recognized commands
def process_command(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif "open song" in command:
        webbrowser.open("https://youtu.be/AWruapvge9A?si=RQ75waYclIYCUOaY")
        speak("Opening Song")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit(0)  # Exit the program
    else:
        speak("Sorry, I did not understand the command. Please try again.")

# Main function to run the assistant
def run_assistant():
    speak("Hello! I'm your voice assistant. How can I help you today?")
    
    while True:
        command = listen_for_command()

        if command:
            process_command(command)
        else:
            speak("Sorry, I couldn't hear your command. Please try again.")

if __name__ == "__main__":
 run_assistant()