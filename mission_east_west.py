from base_robot import *


br = None


def run(br: BaseRobot):
    """
    Execute the custom movement sequence

    Args:
        br (BaseRobot): The robot instance to control
    """

    br.moveLeftAttachmentMotorForDegrees(degrees=150, speedPct=150, waiting=True)
    br.driveForDistance(distance=25, speedPct=80, waiting=True)
    br.turnInPlace(angle=-51, speedPct=45, waiting=True)
    br.driveForDistance(distance=375, speedPct=80, waiting=True)
    br.moveLeftAttachmentMotorForDegrees(degrees=-150, speedPct=150, waiting=True)
    br.leftDriveMotor.run_angle(speed=500, rotation_angle=-170, wait=True)
    br.driveForDistance(distance=750, speedPct=80, waiting=True)
    br.turnInPlace(angle=50, speedPct=45, waiting=True)
    br.moveLeftAttachmentMotorForDegrees(degrees=270, speedPct=150, waiting=True)
    br.turnInPlace(angle=-72, speedPct=45, waiting=True)
    br.driveForDistance(distance=800, speedPct=80, waiting=True)


# If running this file directly (for testing)
if __name__ == "__main__":
    br = BaseRobot()
    print("Starting custom movement mission...")
    print("Press right button to begin")
    # br.waitForRightButton()
    run(br)
