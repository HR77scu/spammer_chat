import pyautogui as pg 
import time

print("progress in 5 seconds ..........")
time.sleep(10)

for i in range(100):
    pg.write(' Halo dunia! ');
    time.sleep(0.5)
    pg.press("enter")