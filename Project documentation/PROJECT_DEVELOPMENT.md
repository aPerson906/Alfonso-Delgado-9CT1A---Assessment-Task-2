# ***Assessment Task 2***

## ***Requirements Outline***


### **Defining the Purpose**

#### The Need
Waking up at 2:00 AM to use the bathroom or other activities and either stubbing your toe in the dark or blinding yourself by turning on the lights and being unable to go back to sleep.

#### Proposed Solution
We will design a lighting system that can be plugged into any room with a power outlet. The system will only activate when it is dark. It uses both motion and light sensors: when motion is detected once dark enough, the light will turn on for 30 seconds before turning back off. If the system detects sufficient light again, such as sunlight or a room light being switched on, it will automatically turn off.

### **Identify Key Actions**

- The microcontroller reads the light sensor to determine whether the room is dark or bright.
- If the room is dark, the microcontroller monitors the motion sensor for movement.
- When movement is detected in the dark, the microcontroller sends a signal to switch the LED light on.
- The microcontroller starts a 30-second timer and keeps the LED on while the timer is running.
- After 30 seconds, the microcontroller switches the LED off. If the light sensor detects enough light (such as sunlight or another light on), the microcontroller keeps the LED off until the room becomes dark again.



### **Functional Requirements**

The machine requires:    
- Light Sensor Input: If light levels are high (daylight or other lights on), the system must remain in sleep mode and keep the LED output off.
- Motion Sensor Input: If the room is dark and the PIR sensor detects human movement, the system must trigger the LED turning on event.
- LED Output: When there's motion detection in the dark, the LED must instantly turn on and project a gentle glow.
- Timer Control: The system must keep the LED illuminated for exactly 30 seconds after motion is detected, then automatically turn the LED off if no further movement is sensed.
- Gentle glow must be 450 lumens to keep brightness down not to affect users eyes or senses. (otherwise could get flashed)




### **Test Cases**


| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Other light source is on and motion sensor detects movement.|Light sensor detects that the room is bright.|LED stays off.|
|No other light source is in the room, motion sensor detects movement.|Light sensor detects that the room is dark, motion sensor detects movement.|LED turns on.|
|Machine emits light, and 30 seconds have passed.|30 second timer is done.|LED turns off. 




### **Non-Functional Requirements**

**Efficiency**
The system should only use power when needed, not wasting energy unecessarily. It should stay off when there is another light ssource present and turn on only when it's dark and motion is detected.

**Response Time**
The light should switch on immediantly (roughly within 1-2 seconds) after motion is detected in a dark room.

**Accuracy**
The system should reliably detect movement in only the dark and emit light when both conditions are met (movement and darkness). It should also turn off exactly in or roughly 30 seconds.







## ***Algorithms***

### Flow chart
![Entire flowchart](images/flowchart.png)


### Pseudocode


    BEGIN 
        REPEAT CONTIONOUSLY
            CALL light()
        END REPEAT

    END


    BEGIN light()
        READ light sensor
        IF light levels <= 50 THEN
            CALL motion()
        ELSE
            OUTPUT LED off
        END IF
    END light()


    BEGIN motion()
        READ motion sensor
        IF motion is detected THEN
            CALL timer()
        ELSE 
            OUTPUT LED off
        END IF
    END motion()


    BEGIN timer()
        OUTPUT LED on
        SET seconds = 0
        WHILE seconds < 30
            WAIT 1 second
            ADD 1 to seconds
        END WHILE
        OUTPUT LED off
    END timer()





## ***Development and Intergration***
***First attempt***

```Python 
from machine import Pin, ADC
import time

light_sensor = ADC(26) # LDR (light sensor) 
motion_sensor = Pin(15, Pin.IN) # PIR (motion sensor)
led = Pin(16, Pin.OUT) # LED (light)
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
 ```


## ***Testing and Debugging***

### **Test Case**

| Test Case | Problems encountered/notes     | Solution   |
|---------- |---------- |----------------   |
|Other light source is on and motion sensor detects movement.|The light sensor (photo cell) was not coded correctly at first, meaning the LED could turn on even when the room was bright. |After testing the photo cell and checking the readings, I found that bright readings were around 544–960 and dark readings were around 1536–1824. I changed the light threshold to 1200 so the LED only activates when it is dark.|
|No other light source is in the room, motion sensor detects movement.|The ultrasonic sensor was too reactive and could detect small changes in distance as movement.|I increased the movement threshold so the sensor needs to detect a bigger change in distance before turning the LED on.|
|Machine emits light, and 30 seconds have passed.|The LED needed to turn off automatically after the 30-second timer finished. (no problem experienced)| I used a timer function with time.sleep(1) and a counter that increases every second until it reaches 30. The LED then turns off automatically.
|Button is pressed to turn the system on/off. (new test case) |The button was not working correctly, not turning off the system when pressed.| I was unable to fix this problem, I suspect that it is because of the wiring.

### **Evaluation of Process**

#### Other Light Source Is On and Movement Is Detected

I was successful in meeting this test case after fixing the photo cell code. I tested the photo cell in both bright and dark conditions and used the readings to choose a threshold of 1200. What went well was that the LED stayed off when the room was bright, even when movement was detected. The main challenge was finding the right threshold for the light sensor.

#### *No Other Light Source Is On and Movement Is Detected*

I successful with this test case, but the ultrasonic sensor was too sensitive at first. I tested it and noticed that it was picking up previous movements, which could cause the LED to turn on when there was no new movement. I fixed this by adding a delay before the sensor checked for movement again, giving the previous movement time to clear.

#### *Machine Emits Light and 30 Seconds Have Passed*

I was successful in meeting this test case and didn't experience any problems. I used time.sleep(1) and a counter to keep track of the 30 seconds before turning the LED off. I tested the timer to make sure the LED stayed on and then switched off after 30 seconds. This part of the program worked well and didn't need any major changes.

#### *Button Is Pressed to Turn the System On/Off*

I was unsuccessful in meeting this test case because the button would not turn the system off when it was pressed. I checked the code and tested the button, but I was unable to find a way to fix the problem. I think the problem may be caused by the wiring rather than the code. I could improve this by checking the button's wiring and making sure it is connected to the correct pins.

### **Final Product**
(Final video is on the classroom, submission site - but can also be found in images)

## ***Evaluation***

### **Peer Evaluation - PMI**

|Plus|Minus|Interesting/Implications|
|---------- |---------- |----------------|
|Easy to understand code      |The button doesn't work properly - making it useless          |The timer helps stop the LED from staying on for too long.            |
|Ultrasonic sensor works very well - allowing movement detection from 10 cm away     |Motion sensor is too reactive            |The LED seems to turn on even when there is no visible movement               |
Reviewed by: Aarav Rangi





|Plus|Minus|Interesting/Implications|
|---------- |---------- |----------------   |
|The LED is quite bright and allows for high visibility within the space.  |  The device's wiring seems comlicated and messy.|The features of the device itself seems to work quite well.|
|The response time of the device is rapid and responsive to objects within feasible distance.| The LED turns off at a seemingly random time so it might come as a shock to see the device just turn off, add and indicator to when it will turn off perhaps.| Although messy the device seemed comprehensive and cohesive so that it was able to be easily used to fit its purpose.|
Reviewed by: Pradhyot Narasimha



### **Final Evaluation**

**Evaluation of Final Test in Relation to Functional Criteria**

In terms of my functional requirements, my final test was mostly successful. The light sensor worked well and was able to detect when the room was dark, keeping the LED off when there was another light source present. The ultrasonic sensor also worked well and was able to detect movement and turn the LED on. The timer also worked as intended and turned the LED off after around 30 seconds. However, the ultrasonic sensor was sometimes too reactive and would detect movement when there was no visible movement. Overall, most of my functional requirements were met, but the movement detection could still be improved.

**Evaluation of Final Test in Relation to Non-Functional Criteria**

In terms of my non-functional requirements, my final test was mostly successful. The system was efficient because the LED only turns on when it is dark and movement is detected, meaning it does not waste power when it is not needed. The response time was also good, as the LED turned on shortly after movement was detected. However, the accuracy could be improved because the ultrasonic sensor was sometimes too sensitive and would turn the LED on when there was no movement. The button also did not work properly, which affected how easy the system was to control. Overall, my system met most of my non-functional requirements, but the accuracy and button could be improved.

**Evaluation of Final Performance in Relation to the Identified Need/Problem**

In terms of identified need, I think my prodduct was successful, The light system helps with the problem of waking up in the dark and having to either walk around in the dark, or blinding yourself with a bright light. The ultrasonic sensor, detects movement when it is dark and turns on a LED for 30 seconds, allowing the user to see in the dark, without blinding themselves. Overall, the system met the main need, but there are still some things that could be improved, such as making the sensor more accurate and reliable. 

**Evaluation of Project in Relation to Project Management**

In terms of my project management, I did not perform well. At the beggining of the task, I did regular pushes - roughly every 2 days, but in the second last week of the task I had a massive gap - from push 9-10, prioritising other assessments. I also did not follow the structure on how to complete the task. I followed the plan at the begginging - Week 1 working on the requirments outline, Week 2 working on flow charts and algorithims,etc but fell behind in Week 4 on my testing and debugging phase, resulting in everything aftwerards, being one week behind schedule - stressing and overwhelming me. I also left many things until the night before the task as due (such as these evaluations). Overall, I should have managed my time better and continued making regular progress throughout the entire task instead of leaving important work until the last minute.

**Evaluation of Project in Relation to Peer Feedback**

In relation to peer feedback, I think most of the feedback was helpful and showed me what worked well and what could be improved. Aarav said that the code was easy to understand and that the ultrasonic sensor worked well for detecting movement, but also pointed out that the motion sensor was too reactive and sometimes turned the LED on when there was no visible movement. Pradhyot also said that the LED was bright and the response time was good, but mentioned that the wiring looked complicated and messy and that the LED turned off unexpectedly. Overall, the feedback showed that the main features of my project worked well, but there were still some areas that could be improved, especially the sensor accuracy, wiring and showing when the timer is about to finish.

**Future Improvements you could make to your Final Product**

If I was able to redo this project I would focus on making consistent pushes and finding a way to make my system efficent and acurrate. I would fix my button so that it works properly, make my wiring more neat and organised, and make the ultrasonic sensor less reactive. I would also try and improve the LED, maybe by making it dim the closer the timer is done, allowing it to be gradual instead of abrupt. I would also try and make my system more reliable overall. 
If I did this I beleive my project would have been succesful, and would've done its purpose even better.

### **Bibliography**
https://randomnerdtutorials.com/raspberry-pi-pico-hc-sr04-micropython/

https://www.youtube.com/watch?v=GkfznA8SCQc

https://www.youtube.com/watch?v=Xn_oAiH0ZsM