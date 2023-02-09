# pixiv 모든 북마크 & 팔로우 비공개 하기
import time
import pyautogui
import os

# print(pyautogui.size()) # 화면 사이즈

def check_mouse_position(): 
    time.sleep(2)
    print(pyautogui.position()) # 마우스 위치

def bookmark_secret(): # 북마크 비공개
    pyautogui.moveTo(3438, 837) # (x, y) 위치로 마우스 바로 이동
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.moveTo(2304, 958) 
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.moveTo(2613, 954) 
    pyautogui.click()
    time.sleep(6)

def follow_secret(): # 팔로우 비공개
    pyautogui.moveTo(2489, 857) # (x, y) 위치로 마우스 바로 이동
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(2463, 639)
    pyautogui.click()
    time.sleep(0.7)

    pyautogui.moveTo(2489, 867) 
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(2463, 649)
    pyautogui.click()
    time.sleep(0.7)

    pyautogui.moveTo(2489, 837) 
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(2463, 619)
    pyautogui.click()
    time.sleep(0.7)

    pyautogui.moveTo(2489, 776) 
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(2463, 558)
    pyautogui.click()
    time.sleep(0.7)   

    pyautogui.moveTo(2489, 889)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(2457, 672)
    pyautogui.click()
    time.sleep(0.7)   

    pyautogui.moveTo(2491, 805) 
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(2486, 586)
    pyautogui.click()
    time.sleep(0.7)   

    pyautogui.moveTo(2306, 582)
    pyautogui.click()
    time.sleep(0.7)   


'''
    pyautogui.locateOnScreen('dot.png', region=(2251, 666, 2648, 947), confidence=0.6)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.locateOnScreen('secret.png', region=(2207, 541, 2648, 947), confidence=0.6)
    pyautogui.click()
    time.sleep(1)
'''

time.sleep(2)
print(check_mouse_position())
# os.chdir('C:/Users/alawho/Documents/GitHub/pyautogui')
for _ in range(29): #31
    follow_secret()
    print("done")
    # bookmark_secret()

'''
# 컴퓨터 종료
pyautogui.moveTo(1946, 1061) 
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1947, 1019) 
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(2008, 938)
pyautogui.click()
time.sleep(1)   
'''