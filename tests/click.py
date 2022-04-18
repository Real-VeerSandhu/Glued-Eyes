import pyautogui
import time

w = 2560
h = 1440

print('Count down:')
for i in range(3):
    print(f'{3-i}...')
    time.sleep(1)
pyautogui.moveTo(w/2,h/2)

counter = 0
for i in range(10):
    pyautogui.click(clicks=1, interval=0.01)
    counter += 1

print('\nDone...')
print(pyautogui.size())