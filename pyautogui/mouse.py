import time
import pyautogui

def check_mouse_position(): 
    time.sleep(2)
    print(pyautogui.position()) # 마우스 위치

def auto_click():
    pyautogui.click()
    time.sleep(0.1)

def mid_click():
    pyautogui.moveTo(2489, 837) 
    pyautogui.middleClick()
    time.sleep(40)

# time.sleep(2)
# print(check_mouse_position())
for _ in range(500):
    auto_click()

