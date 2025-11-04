# MEASURE PATH TOOL
# This utility script helps measure robot movements and alignment for mission planning.
#
# WHAT IT DOES:
# - Continuously displays the robot's current heading (rotation angle) and distance traveled
# - Automatically resets measurements when the robot stops moving
# - Provides audio feedback (beep) when measurements are updated
#
# HOW TO USE:
# 1. Place the robot at your starting position
# 2. Run this script on the robot
# 3. Push/drive the robot manually to measure distances and angles
# 4. Press the BLUETOOTH button to reset measurements to zero at any time
# 5. The hub will beep and display measurements when the robot stops moving
#
# USEFUL FOR:
# - Measuring field distances for mission planning
# - Checking robot alignment and heading accuracy
# - Calibrating turn angles and drive distances
# - Verifying robot positioning during mission development
#
# NOTE: Distance is calculated using the wheel diameter (88.9mm) and displayed in cm

from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Button
from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from utils import TIRE_DIAMETER

from base_robot import *

br = BaseRobot()


# Function to reset motors and IMU
def reset_robot():
    br.hub.imu.reset_heading(0.0)
    br.leftDriveMotor.reset_angle(0)
    br.rightDriveMotor.reset_angle(0)
    br.robot.reset()
    print("IMU and motors reset to 0")


# Function to print the current heading and stats
def print_heading():
    heading = br.hub.imu.heading()
    print("Current heading:", round(heading, 1))


def print_stats():
    heading = br.hub.imu.heading()
    left_angle = br.leftDriveMotor.angle()
    right_angle = br.rightDriveMotor.angle()

    left_distance = left_angle * 3.14159 * TIRE_DIAMETER / 360
    right_distance = right_angle * 3.14159 * TIRE_DIAMETER / 360

    avg_distance = (left_distance + right_distance) / 2

    print("Heading: ", round(heading, 1))
    print("Distance: ", round(avg_distance / 10, 1))


# Initialize the reset at the start
reset_robot()

display = True
while True:
    # Check if the center button (bluetooth equivalent in this context) is pressed
    if Button.BLUETOOTH in br.hub.buttons.pressed():
        # Reset the robot when the button is pressed
        reset_robot()
        # Wait for a short duration to prevent accidental multiple presses
        wait(500)
        display = True

    # If this hub is stationary, print the current heading once
    if display and br.hub.imu.stationary():
        print_stats()
        display = False
        # Make the hub beep
        br.hub.speaker.beep()

    elif not br.hub.imu.stationary():
        display = True
