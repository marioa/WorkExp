
import time
import pyautogui

# Give yourself 5 seconds to click into a text box, editor, or browser window
time.sleep(5)

# Automatically type the phrase at the current cursor/focus location
pyautogui.write("I am a hard working Programmer", interval=0.05)
