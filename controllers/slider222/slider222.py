from controller import Robot

# Create a robot instance
robot = Robot()

# Get the time step of the simulation
timestep = int(robot.getBasicTimeStep())

# Get the linear motor
linear_motor = robot.getDevice('lm')
ps_sensor = robot.getDevice('ps')
lm_sensor = linear_motor.getPositionSensor()
lm_sensor.enable(timestep) 

# Set the target position and velocity for the linear motor
target_position = 0  # Adjust as needed
target_velocity = 0.1  # Adjust as needed
initial_position = abs(lm_sensor.getValue())
print("initial is:", initial_position)

linear_motor2 = robot.getDevice('lmm')
ps_sensor2 = robot.getDevice('pss_sensor')
lm_sensor2 = linear_motor.getPositionSensor()
lm_sensor2.enable(timestep) 
target_position2 = 0.16

# Get the motors for the tires
motor1 = robot.getDevice('motor1')
motor2 = robot.getDevice('motor2')
motor3 = robot.getDevice('motor3')
motor4 = robot.getDevice('motor4')

print("motor joint")
motor1.setPosition(float('inf'))
motor2.setPosition(float('inf'))
motor3.setPosition(float('inf'))
motor4.setPosition(float('inf'))
motor1.setVelocity(0.0)
motor2.setVelocity(0.0)
motor3.setVelocity(0.0)
motor4.setVelocity(0.0)

# Set up the maximum motor velocity
max_velocity = 8.28
if linear_motor2 is None:
    print("Error: Could not find linear motor device 'lm2'")
else:
    # Set the position and velocity of linear_motor2
    linear_motor2.setPosition(target_position2)
    linear_motor2.setVelocity(target_velocity)


# Main control loop
while robot.step(timestep) != -1:
    while robot.step(timestep) != -1:
        linear_motor2.setPosition(target_position2)
        linear_motor.setVelocity(target_velocity)
        lm2final = lm_sensor2.getValue()
        # print("m : " , lm2final)
        
    if lm2final >= target_position2:
        linear_motor.setPosition(target_position)
        linear_motor.setVelocity(target_velocity)
    
    # If the motor has moved away from the normal position
    current_position = lm_sensor.getValue()
    print("CURRENT : " , current_position)  
    if current_position >= 2.2341855153899832:
        print("Reached target position:", current_position)
        linear_motor.setPosition(0.8222486449744286)
        linear_motor.setVelocity(target_velocity)
        motor1.setVelocity(max_velocity)
        motor2.setVelocity(max_velocity)
        motor3.setVelocity(max_velocity)
        motor4.setVelocity(max_velocity)