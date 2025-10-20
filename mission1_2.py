from base_robot import *

# Custom Movement Sequence Mission
# This mission performs the following sequence:
# 1. Go forward 65cm
# 2. Turn -40 degrees (left)
# 3. Go forward 10cm
# 4. Go backward 23cm
# 5. Turn 40 degrees (right)
# 6. Go backward 65cm
#
# Robot Alignment: Place robot at desired starting position
# No special arm positions or attachments needed

br = None

def run(base_robot):
    global br
    br = base_robot
    
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    br.driveForDistance(distance=740, speedPct=90, then=Stop.BRAKE, waiting=True)

    # Step 2: Turn -40 degrees (left turn)
    br.turnInPlace(angle=-50, speedPct=60, waiting=True)

    # Step 3: Go forward 20cm (200 mm)
    br.driveForDistance(distance=150, speedPct=90, then=Stop.BRAKE, waiting=True)

    # Step 4: Go backward 23cm (230 mm)
    br.driveForDistance(distance=-230, speedPct=90, then=Stop.BRAKE, waiting=True)

    # Step 5: Turn 40 degrees (right turn)
    br.turnInPlace(angle=45, speedPct=50, waiting=True)

    # Step 6: Go backward 65cm (650 mm)
    br.driveForDistance(distance=-650, speedPct=80, then=Stop.BRAKE, waiting=True)

    # Mission complete - beep to indicate success


if __name__ == "__main__":
    br = BaseRobot()
    run(br)
