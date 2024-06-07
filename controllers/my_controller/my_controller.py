"""my_controller controller."""

# Muhammad Taqui
# Babar Ali
# ROBOTICS Semester Project - "WALL FOLLOWING ROBOT" (Basic)
# Deadline: 6 June 2024


#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

def run_robot(robot):
    """WALL FOLLOWING ROBOT"""
    
    #get the time
    timestep = int(robot.getBasicTimestep())
    max_speed = 6.28
    
    #ENABLE MOTORS
    left_motor = robot.getmotor('left wheel robot')
    right_motor = robot.getmotor('right wheel robot')

    left_motor.setPosition(float('inf')
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    #ENABLE SENSORS
    prox_sensor = []
    for ind in range(8):
        sensor_name = 'ps' + str(ind)
        prox_sensors.append(robot.getDistanceSensor(sensor_name))
        prox_sensors[ind].enable(timestep)
        
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        for ind in range(8):
            print("ind: {}, val: []".format(ind,prox_sensors[ind].getValue())) 

        # Process sensor data here.

        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        left_motor.setVelocity(max_speed)
        right_motor.setVelocity(max_speed)

     # Enter here exit cleanup code.

if __name __ == "__main__"
     
     #ROBOT INSTANCE
     my_robot = Robot()
     run_robot(my_robot)