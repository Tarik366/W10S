import get_kb_lang
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

import pyautogui
import time
import pyperclip

def send_keys(keys):
    pyperclip.copy(keys)
    pyautogui.hotkey('ctrl', 'v')

# recognize speech using Google
try:
    translated_text = r.recognize_google(audio, language=get_kb_lang.get_language_id())
    print(translated_text)
    send_keys(translated_text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
