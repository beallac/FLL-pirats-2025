from base_robot import *
br = BaseRobot()

# Reset the heading to 0 degrees at the start of the program.
br.hub.imu.reset_heading(0.0)

# Function to print the current heading
def print_heading():
    heading = br.hub.imu.heading()
    print("Current heading:", heading)

# Drive forward by 500mm (half a meter).
print_heading()
br.robot.straight(500)

# Turn around clockwise by 180 degrees.
print_heading()
br.robot.turn(180)

# Drive forward again to get back to the start.
print_heading()
br.robot.straight(500)

# Turn around counterclockwise.
print_heading()
br.robot.turn(-180)

