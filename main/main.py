from machine import Pin, ADC
import time


light_sensor = ADC(26) # LDR (light sensor) 
motion_sensor = Pin(15, Pin.IN) # PIR (motion sensor)
led = Pin(16, Pin.OUT) # LED (light)



# light_levels function
def light():
    if light_sensor <= 50:
        motion_detect()
    else:
        light()

# timer funtion 
def seconds():
    while time <= 30:
        time + 1
        time.sleep(1)
    time.sleep(2) # A 2 second delay
    light()

# motion_detect function
def motion_detect():
    if motion_sensor.value() == 1:  #If motion_sensor value = 1 then motion is detected
        seconds()
    else:
        light()