from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from utils import TIRE_DIAMETER, AXLE_TRACK

STRAIGHT_SPEED = 400  # normal straight speed for driving, mm/sec
STRAIGHT_ACCEL = 600  # normal acceleration, mm/sec^2
TURN_RATE = 150  # normal turning rate, deg/sec
TURN_ACCEL = 360  # normal turning acceleration, deg/sec^2

# Initialize the hub
hub = PrimeHub()

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)

# Initialize the drive base using project constants
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=TIRE_DIAMETER, axle_track=AXLE_TRACK)
drive_base.settings(STRAIGHT_SPEED, STRAIGHT_ACCEL, TURN_RATE, TURN_ACCEL)
drive_base.use_gyro(True)

# Reset the heading to 0 degrees at the start of the program.
hub.imu.reset_heading(0.0)

# Function to print the current heading
def print_heading():
    heading = hub.imu.heading()
    print("Current heading:", heading)

# Drive forward by 500mm (half a meter).
print_heading()
drive_base.straight(500)

# Turn around clockwise by 180 degrees.
print_heading()
drive_base.turn(180)

# Drive forward again to get back to the start.
print_heading()
drive_base.straight(500)

# Turn around counterclockwise.
print_heading()
drive_base.turn(-180)
