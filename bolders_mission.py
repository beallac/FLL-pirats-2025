from base_robot import *

# Custom Sequence Mission:
# 1. Goes forward 69 cm (690 mm)
# 2. Turns 44 degrees left
# 3. Forward 10 cm (100 mm)
# 4. Turns 153 degrees right
#
# Robot Alignment: Place robot at desired starting position
# No special arm positions or attachments needed


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    # Step 1: Drive forward 69 cm (690 mm) at 80% speed
    br.driveForDistance(distance=670, speedPct=80, then=Stop.BRAKE, waiting=True)

    # Step 2: Turn 44 degrees left (negative for left turn)
    br.turnInPlace(angle=-44, speedPct=50, waiting=True)

    # Step 3: Drive forward 10 cm (100 mm) at 80% speed
    br.driveForDistance(distance=130, speedPct=80, then=Stop.BRAKE, waiting=True)

    # Step 4: Turn 153 degrees right (positive for right turn)
    br.turnInPlace(angle=100, speedPct=50, waiting=True)

    br.driveForDistance(distance=30, speedPct=40, then=Stop.BRAKE, waiting=True)

    br.turnInPlace(angle=40, speedPct=75, waiting=True)

    # Mission complete - optional beep to indicate completion
    print("Custom sequence mission complete!")


# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
