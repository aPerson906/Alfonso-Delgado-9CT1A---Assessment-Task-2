from machine import Pin, ADC
import time


light_sensor = ADC(26) # LDR (light sensor) 
motion_sensor = Pin(15, Pin.IN) # PIR (motion sensor)
led = Pin(16, Pin.OUT) # LED (light)


#LIght sensor function
def light():
    light_level = light_sensor.read_u16()  

    if light_level <= 50: # Reads light levels if they are above 50 then move onto motion detect func
        motion_detect()
    else:
        led.off()   

# timer funtion 
def seconds():
    led.on()

    timer = 0
    while timer < 30: #while the timer is less than 30 add 1 more second until it is 30 or above then turn LED off
        time.sleep(1) # 1 second delay
        timer += 1

    led.off()


# motion_detect function
def motion_detect():
    if motion_sensor.value() == 1:   # #If motion_sensor value = 1 then motion is detected
        seconds()
    else:
        led.off()

# Main program
while True:
    light()
    time.sleep(0.1)
