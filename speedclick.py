from pynput.mouse import Controller, Button
import time
mouse =  Controller()
mouse.position = (1000,500)
a=0
while a<1000000:
    mouse.click(Button.left,10)
    a+=1
    time.sleep(0.00000000000000000001)

