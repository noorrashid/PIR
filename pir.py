import time
from gpiozero import MotionSensor
from gpiozero import Buzzer 
from gpiozero import LED 
pir = MotionSensor(4)
buzzer = Buzzer(17)
red=LED(25)
i = 0
while True:
    if pir.wait_for_motion():
        i+=1
        print(f"you moved {i}")
        buzzer.on()
        red.on()
        time.sleep(1)
        buzzer.off()
        red.off ()
    if pir.wait_for_no_motion():
        print("No motion")

