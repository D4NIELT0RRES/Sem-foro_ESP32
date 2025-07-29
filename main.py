from machine import Pin 
from utime import sleep

print("Hello, ESP32!")

led_green = Pin(17, Pin.OUT)
led_yellow = Pin(16, Pin.OUT)
led_red = Pin(15, Pin.OUT)




while True:

    led_green.on()
    sleep(20)
    led_green.off()
    led_yellow.on()
    sleep(10)
    led_yellow.off

    led_red.on()
    sleep(7)
    led_red.off()
    

    

    

    

   

    


