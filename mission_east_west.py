from base_robot import *


br = None


def run(br: BaseRobot):
    """
    Execute the custom movement sequence

    Args:
        br (BaseRobot): The robot instance to control
    """

    br.driveForDistance(distance=25, speedPct=80, waiting=True)
    br.turnInPlace(angle=-33.5, speedPct=45, waiting=True)
    br.driveForDistance(distance=285, speedPct=80, waiting=True)
    br.turnInPlace(angle=-20, speedPct=45, waiting=True)
    br.moveLeftAttachmentMotorForDegrees(degrees=250, speedPct=150, waiting=True)
    br.turnInPlace(angle=35, speedPct=45, waiting=True)
    br.driveForDistance(distance=75, speedPct=80, waiting=True)
    br.turnInPlace(angle=-48, speedPct=45, waiting=True)
    br.driveForDistance(distance=120, speedPct=80, waiting=True)
    br.turnInPlace(angle=-9.7, speedPct=45, waiting=True)
    br.moveLeftAttachmentMotorForDegrees(degrees=-550, speedPct=150, waiting=True)
    br.turnInPlace(angle=-25.75, speedPct=45, waiting=True)
    br.driveForDistance(distance=700, speedPct=80, waiting=True)
    br.turnInPlace(angle=55, speedPct=45, waiting=True)
    br.moveLeftAttachmentMotorForDegrees(degrees=285, speedPct=150, waiting=True)
    br.turnInPlace(angle=-58.5, speedPct=45, waiting=True)
    br.driveForDistance(distance=700, speedPct=80, waiting=True)


# If running this file directly (for testing)
if __name__ == "__main__":
    br = BaseRobot()
    print("Starting custom movement mission...")
    print("Press right button to begin")
    # br.waitForRightButton()
    run(br)
