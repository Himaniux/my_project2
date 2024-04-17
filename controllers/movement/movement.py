"""movement controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left_motor')
right_motor = robot.getDevice('right_motor')
max_velocity = 6.28  # Adjust as needed
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Main control loop
while robot.step(timestep) != -1:
    # Set the velocities of the left and right motors to move forward
    left_motor.setVelocity(max_velocity)
    right_motor.setVelocity(max_velocity)
    pass

# Enter here exit cleanup code.
