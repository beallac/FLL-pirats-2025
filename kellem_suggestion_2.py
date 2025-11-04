from base_robot import *

# Set br to None at the top (required for menu structure)
br = None


def run(base_robot):
    """Combined Maze Code - Main mission function"""
    global br  # Tells Python we want to use the br defined at the top
    br = base_robot  # Links the passed-in robot to br

    # West-East navigation script
    # Exit home area
    br.driveForDistance(distance=40, speedPct=40)
    # Turn towards
    br.turnInPlace(angle=-54.6, speedPct=40)
    br.driveForDistance(distance=420.8, speedPct=40)
    br.moveLeftAttachmentMotorForDegrees(degrees=-102, speedPct=100)
    br.turnInPlace(angle=-33.75, speedPct=40)
    br.driveForDistance(distance=960, speedPct=40)
    br.turnInPlace(angle=40, speedPct=40)
    br.driveForDistance(distance=-120, speedPct=40)
    br.turnInPlace(angle=50, speedPct=40)
    br.moveLeftAttachmentMotorForDegrees(degrees=882, speedPct=40)
    br.driveForDistance(distance=82, speedPct=40)
    br.turnInPlace(angle=90, speedPct=40)
    br.driveForDistance(distance=178, speedPct=40)
    br.turnInPlace(angle=-90, speedPct=40)
    br.driveForDistance(distance=-90, speedPct=40)
    br.moveLeftAttachmentMotorForDegrees(degrees=-882, speedPct=40)
    br.driveForDistance(distance=22, speedPct=40)
    br.moveLeftAttachmentMotorForDegrees(degrees=882, speedPct=40)


if __name__ == "__main__":
    br = BaseRobot()
    print("Starting custom movement mission...")
    print("Press right button to begin")
    # br.waitForRightButton()
    run(br)
