import speech_recognition as sr
import pyttsx3
from langgraph.graph import GraphExecutor
from graph import graph
from state import State

# Initialize speech recognition and TTS
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
executor = GraphExecutor(graph)

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to get speech input from the user
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio)
            print(f"User said: {user_input}")
            return user_input
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def main():
    initial_state = State(messages=[], location="", preferences={})
    
    while True:
        speak("How can I assist you today?")
        user_input = listen()
        if user_input.lower() in ["exit", "quit"]:
            speak("Goodbye!")
            break
        initial_state['messages'].append({"role": "user", "content": user_input})
        final_state = executor.run(initial_state)
        response = final_state['messages'][-1]['content']
        print(response)
        speak(response)

if __name__ == "__main__":
    main()
