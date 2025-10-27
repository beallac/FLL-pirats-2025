from base_robot import *


br = None


def run(br: BaseRobot):
    """
    Execute the custom movement sequence

    Args:
        br (BaseRobot): The robot instance to control
    """

    br.driveForDistance(distance=25, speedPct=80, waiting=True)

    br.turnInPlace(angle=-52, speedPct=45, waiting=True)

    br.driveForDistance(distance=415, speedPct=80, waiting=True)

    br.moveLeftAttachmentMotorForDegrees(degrees=-150, speedPct=150, waiting=True)

    br.turnInPlace(angle=-33.75, speedPct=45, waiting=True)

    br.driveForDistance(distance=700, speedPct=80, waiting=True)

    br.turnInPlace(angle=55, speedPct=45, waiting=True)

    br.moveLeftAttachmentMotorForDegrees(degrees=250, speedPct=150, waiting=True)

    br.turnInPlace(angle=-65, speedPct=45, waiting=True)

    br.driveForDistance(distance=630, speedPct=80, waiting=True)

    br.moveLeftAttachmentMotorForDegrees(degrees=-100, speedPct=150, waiting=True)


# If running this file directly (for testing)
if __name__ == "__main__":
    br = BaseRobot()
    print("Starting custom movement mission...")
    print("Press right button to begin")
    # br.waitForRightButton()
    run(br)
