# light_levels function
# motion_detect function
# timer function

def motion_detect():
    motion_sensor = input ("insert")
    while motion_sensor == True: #while motion detetector senses motion
        print("LED on") #Put's light/LED on
        timer()
    else:
        light_levels() #otherwise go back and check light levels

def light_levels():
    light_sensor = input('insert')
    while light_sensor == True: #while light sensor decects light
        light_levels() #loop back
    else:
        motion_detect() #send signal to motion dectector to check motion

def timer():
    print("hi")
