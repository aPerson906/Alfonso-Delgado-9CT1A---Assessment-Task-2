# ***Assessment Task 2***

## ***Requirements Outline***


### **Defining the Purpose**

#### The Need
Waking up at 2:00 AM to use the bathroom or other activities and either stubbing your toe in the dark or blinding yourself by turning on the lights.

#### Proposed Solution
We will design a light system to put in any room with an outlet which will emit light only when its dark. It'll use motion and light sensors and once distrub by movement it'll emit lights, for 30 seconds. Afterwards it'll dim again. Once it detects light again - such as from the sun or from a lightbulb - it'll turn off.
(fix)

### **Identify Key Actions**

4 Specific actions the microcontroller needs to perform to complete this task is:

- The microcontroller checks the light sensor to determine if the room is currently dark or bright.
- If the light sensor confirms the room is dark, the microcontroller activates and monitors the motion sensor for any movement.
- When the movement sensor detects movement in the dark, the microcontroller sends a signal to turn on the light.
- The microcontroller starts a 30-second timer the moment motion is detected, keeping the LED on for that duration, and then switches the LED off automatically once the time expires
(fix)

List at least 3-5 specific actions which your microcontroller needs to perform to complete the task. These should be clear, simple actions like detection, input, output or triggering an event (e.g. sound or lights).



### **Functional Requirements**

The machine requires    
- Light Sensor Input: If light levels are high (daylight or other lights on), the system must remain in sleep mode and keep the LED output off.
- Motion Sensor Input: If the room is dark and the PIR sensor detects human movement, the system must trigger the LED turning on event.
- LED Output: When there's motion detection in the dark, the LED must instantly turn on and project a gentle glow.
- Timer Control: The system must keep the LED illuminated for exactly 30 seconds after motion is detected, then automatically turn the LED off if no further movement is sensed.
- Gentle glow must be 450 lumens to keep brightness down not to affect users eyes or senses. (otherwise could get flashed)


A functional requirement is the action or behavior the robot needs to perform.
For each key action, write a functional requirement that clearly states what the robot must do. These should be written in a clear and concise manner.
(fix)


### **Test Cases**


| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Other light source is on and motion sensor detects movement.|Light sensor reads light source.|No light appears from the machine.|
|No other light source is in the room, motion sensor detetcs movement.|Light sensor reads light source, motion sensor reads motion.|Light appears from the machine.|
|Machine emits light, motion sensor stops detecting motion.|Motion sensor stops reading motion, stopwatch starts.|Emitted light turns off after 30 seconds. 
(fix)


For each functional requirement, develop tese cases for it. A test case is simply an outline of expected function, input and outputs, so that we can test against it later on when developing prototypes.

Identify the inputs (e.g. sensor data, button presses).

Identify the expected outputs (e.g. motor movement, sound, display messages).
(table)



### **Non-Functional Requirements**
`

These are requirements that focus on how well the robot will perform in completing the task, rather than the completing of the task itself. Consider the following: 

Efficiency

Response Time

Accuracy








## ***Algorithms***
Pseudocode and Flowchart development (include images for Flowchart)

(insert flowchart and pseudocode)


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

### **Final EValuation**