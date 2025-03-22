import pyautogui
import time

# Wait for 4 seconds to give you time to focus on the correct window
time.sleep(4)

count = 0 
while count < 100:
    # Type the message
    pyautogui.typewrite("Sahil pagal hai")
    # Press the enter key main bhi latata wait
    pyautogui.press("enter")
count += 1
