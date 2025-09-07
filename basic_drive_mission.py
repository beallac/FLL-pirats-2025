from base_robot import *

# Basic Drive Mission: 
# - Drive forward 1 meter (1000 mm)
# - Turn 180 degrees to face the opposite direction
# - Drive back 1 meter to return to starting position
# 
# Robot Alignment: Place robot at desired starting position
# No special arm positions or attachments needed


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below

    # Drive forward 1 meter (1000 mm) at 80% speed
    br.driveForDistance(
        distance=900, speedPct=80, then=Stop.BRAKE, waiting=True
    )

    # Turn 180 degrees in place to face the opposite direction
    br.turnInPlace(angle=180, speedPct=50, waiting=True)

    # Drive forward 1 meter (1000 mm) again to return to starting position
    br.driveForDistance(
        distance=900, speedPct=80, then=Stop.BRAKE, waiting=True
    )

    br.turnInPlace(angle=-180, speedPct=75, waiting=True)


# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
