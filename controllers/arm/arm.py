"""arm controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()
timestep=64

m=robot.getDevice("motor")
m.setPosition(float('inf'))
m.setVelocity(0.0)

ps=robot.getDevice("ps")
ps.enable(timestep)

left_motor = robot.getDevice('left_motor')
right_motor = robot.getDevice('right_motor')
max_velocity = 10  # Adjust as needed
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

speed=1
i=0

while(robot.step(timestep)!=-1):
    m.setVelocity(speed)
    i=ps.getValue()
    left_motor.setVelocity(max_velocity)
    right_motor.setVelocity(max_velocity)
    
    if i <= 61.466755411399774:  # Adjust the threshold as needed
        speed = 1
      
    elif i >= 64.5:  # Check if crossed 64.5 upwards
        
        speed = -1

    # if i <= 61.4:  # Adjust the threshold as needed
        # speed = -1
    # elif i >= 64.5:
        # print("hello")  # New condition to check if crossed 58.5 downwards
        # speed = -1
   
  
     
    pass
    
   