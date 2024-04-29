from controller import Robot, Motor # type: ignore

# Create a robot instance
robot = Robot()

# Get the time step of the simulation
timestep = int(robot.getBasicTimeStep())

# Get the linear motor
pullBackMotor: Motor = robot.getDevice('lm')
ps_sensor = robot.getDevice('ps')
lm_sensor = pullBackMotor.getPositionSensor()
lm_sensor.enable(timestep) 

# Set the target position and velocity for the linear motor
target_pull_position = 0.25  # Adjust as needed
target_velocity = 0.1  # Adjust as needed
initial_position = abs(lm_sensor.getValue())
print("initial is:", initial_position)

pickUpMotor: Motor = robot.getDevice('pickupMotor')
ps_sensor2 = robot.getDevice('psPickup')
lm_sensor2 = pickUpMotor.getPositionSensor()
lm_sensor2.enable(timestep) 
target_pickup_position = 0.3
target_pullback_position = 2.2341855153899832

# Get the motors for the tires
motor1: Motor = robot.getDevice('motor1')
motor2: Motor = robot.getDevice('motor2')
motor3: Motor = robot.getDevice('motor3')
motor4: Motor = robot.getDevice('motor4')

print("motor joint")
motor1.setPosition(float('inf'))
motor2.setPosition(float('inf'))
motor3.setPosition(float('inf'))
motor4.setPosition(float('inf'))
motor1.setVelocity(0.0)
motor2.setVelocity(0.0)
motor3.setVelocity(0.0)
motor4.setVelocity(0.0)

ds_f = robot.getDevice('ds_f')
ds_f.enable(timestep)
ds_r = robot.getDevice('ds_r')
ds_r.enable(timestep)
ds_l = robot.getDevice('ds_l')
ds_l.enable(timestep)



# Set up the maximum motor velocity
max_velocity = 8.28
max_turn_velocity = 3.30
# if pickUpMotor is None:
#     print("Error: Could not find linear motor device 'lm2'")
# elif pickUpMotor is not None:
#     # Set the position and velocity of linear_motor2
#     pickUpMotor.setPosition(target_pickup_position)
#     pickUpMotor.setVelocity(target_velocity)

i=0
readyToPullBack = False
readyToPush = False
readyToMoveBed = False
# Main control loop
while robot.step(timestep) != -1:
    pullBackSensor = lm_sensor.getValue()
    pickupSensor = lm_sensor2.getValue()

    # print(f"{pickupSensor} {'not reached' if pickupSensor < target_pickup_position else 'reached'}")
    pickUpMotor.setPosition(target_pickup_position + 0.025)
    pickUpMotor.setVelocity(target_velocity)
    if pickupSensor >= target_pickup_position:
        readyToPush = True
        i += 1
        # if pickUpMotor is not None:
        # if  pullBackSensor >= 2.2341855153899832:
        #     reached = True
        
    # If the motor has moved away from the normal position
    ds_l_val = ds_l.getValue()
    ds_r_val = ds_r.getValue()
    ds_f_val = ds_f.getValue()
    print(f'left: {ds_l_val}, right: {ds_r_val}, front: {ds_f_val}')

    if readyToPush and i > 30:
        if not readyToPullBack:
            pullBackMotor.setPosition(target_pull_position)
            pullBackMotor.setVelocity(target_velocity)
            if pullBackSensor >= target_pullback_position:
                readyToPullBack = True
                i = 0
        else:
            pickUpMotor.setPosition(0.18)
            pickUpMotor.setVelocity(target_velocity)
            pullBackMotor.setPosition(0.0)
            pullBackMotor.setVelocity(target_velocity)
            i += 1
            # print(f"{pullBackSensor}")
            if i > 150:
                motor1.setVelocity(max_velocity)
                motor2.setVelocity(max_velocity)
                motor3.setVelocity(max_velocity)
                motor4.setVelocity(max_velocity)

                # time.sleep(10)
                # pullBackMotor.setPosition(target_pull_position)
                # pullBackMotor.setVelocity(target_velocity)

                # if ds_l_val >= ds_r_val :
                #     motor1.setVelocity(max_velocity)
                #     motor2.setVelocity(-max_velocity)
                #     motor3.setVelocity(-max_velocity)
                #     motor4.setVelocity(max_velocity)
                #     print("turning left")
                # if ds_l_val <= ds_r_val :
                #      motor1.setVelocity(max_velocity)
                #      motor2.setVelocity(-max_velocity)
                #      motor3.setVelocity(max_velocity)
                #      motor4.setVelocity(-max_velocity)
                #      print("turning RIGHT")

            

                # if ds_r_val >= 166 :
                #     motor1.setVelocity(max_velocity)
                #     motor2.setVelocity(max_velocity)
                #     motor3.setVelocity(max_velocity)
                #     motor4.setVelocity(max_velocity)
                #     print("turning front")

                if ds_f_val == 206.339 and ds_l_val == 168.71  and ds_r_val == 243.968 :
                    motor1.setVelocity(max_velocity * 0.8)
                    motor2.setVelocity(max_velocity)
                    motor3.setVelocity(max_velocity)
                    motor4.setVelocity(max_velocity * 0.8)
                    print("turning front") 
                    
                if ds_f_val < 0.2:  # If obstacle detected in front
                     if ds_l_val < ds_r_val:  # If more space on the left
                        motor1.setVelocity(-max_turn_velocity)
                        motor2.setVelocity(max_turn_velocity)
                        motor3.setVelocity(max_turn_velocity)
                        motor4.setVelocity(-max_turn_velocity)
                     else:  # If more space on the right or equal
                        motor1.setVelocity(max_turn_velocity)
                        motor2.setVelocity(-max_turn_velocity)
                        motor3.setVelocity(-max_turn_velocity)
                        motor4.setVelocity(max_turn_velocity)
                else:  # Move forward
                    motor1.setVelocity(max_velocity)
                    motor2.setVelocity(max_velocity)
                    motor3.setVelocity(max_velocity)
                    motor4.setVelocity(max_velocity)