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
Write your first program and include it as a code block in Markdown after you have first successfully run a program (even if it does not achieve the task set out to do). 


## ***Testing and Debugging***
Copy your code from every subsequent test into a code block in Markdown. You will be provided with an evaluation scaffold to reflect on each test. 

### **Test Case**
Choose a test case
Write a brief outline of what you need to do to meet the requirements of the test case.

### **Evaluate**

Adjust and test your code until you meet the requirements of the test case.
Evaluate your process.


## ***Evaluation***
Provide peer evaluations from other team members.

Provide an individual project evaluation in relation to peer feedback, achievement of functional and non-functional requirements, final performance, project management and suggestions for future improvement.

### **Peer Evaluation - PMI**

### **Final Evaluation**