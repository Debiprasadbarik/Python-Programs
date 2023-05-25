import pyautogui as pa
import time
time.sleep(5)
txt= open('animals.txt')
for i in txt:
    pa.write(' '+i)
    pa.press('Enter')


