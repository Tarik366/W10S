import keyboard
import os

def my_function():
    os.system('python gui.py')

keyboard.add_hotkey('super + h', my_function)
keyboard.wait('')
