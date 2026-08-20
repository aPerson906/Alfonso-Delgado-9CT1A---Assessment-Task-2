from machine import Pin, ADC, time_pulse_us
import time

#sets up the pins for the sensors and LED
light_sensor = ADC(26) # LDR (light sensor) 
trig = Pin(15, Pin.OUT)  # TRIG
echo = Pin(17, Pin.IN)   # ECHO
led = Pin(16, Pin.OUT) # LED (light)
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Button
system_on = True # The light starts turned on


#LIght sensor function
def light():
    light_level = light_sensor.read_u16()  

    if light_level >= 1200: # Reads light levels if they are above 1200 then move onto motion detect function
        motion_detect()
    else:
        led.off()   

# timer funtion 
def seconds():
    led.on()

    timer = 0
    while timer < 30:
    #while the timer is less than 30 add 1 more second until it is 30 or above then turn LED off
        time.sleep(1) # 1 second delay
        timer += 1

    led.off()

# distance function
def distance():
    # Send a short signal to the ultrasonic sensor
    trig.value(0) 
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # Measure how long the echo takes
    duration = time_pulse_us(echo, 1)

    # Convert the time into distance
    distance = (duration * 0.0343) / 2

    return distance

# motion_detect function
def motion_detect():
    starting_distance = distance()
    time.sleep(1)
    current_distance = distance()
    if current_distance > starting_distance + 10 or current_distance < starting_distance - 10:
        seconds()
    else:
        led.off()

# Main program
while True:
    # Button pressed
    if button.value() == 0:
        system_on = not system_on
        # Wait until button is released
        while button.value() == 0:
            time.sleep(0.01)
        time.sleep(0.2)
    if system_on:
        light()
    else:
        led.off()
    time.sleep(0.1)
        