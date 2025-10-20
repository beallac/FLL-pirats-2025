from base_robot import *

# Custom movement script that performs the following sequence:
# 1. Goes forward 55.5 mm
# 2. Turns right 56.4 degrees
# 3. Goes forward 21.2 mm
#
# To run this script:
# 1. Make sure the robot is properly aligned at the starting position
# 2. Run this script from the master program or execute it directly


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Step 1: Go forward 55.5 mm
    br.driveForDistance(distance=555, speedPct=80, then=Stop.BRAKE, waiting=True)

    # Step 2: Turn right 56.4 degrees
    br.turnInPlace(57.5)

    # Step 3: Go forward 21.2 mm
    br.driveForDistance(distance=285, speedPct=80, then=Stop.BRAKE, waiting=True)

    # Step 4: Move front attachment left for 2 seconds
    br.moveLeftAttachmentMotorForMillis(millis=2000, speedPct=80)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
