from base_robot import *

# Robot starting position: Place robot at starting line, facing forward


def Run(br: BaseRobot):
    """
    Execute the custom movement sequence

    Args:
        br (BaseRobot): The robot instance to control
    """

    # Step 1:
    print("Step 1: Driving forward 1.5 cm")
    br.driveForDistance(distance=15, speedPct=80, waiting=True)

    # Step 2:
    print("Step 2: Turning left 20 degrees")
    br.turnInPlace(angle=-20, speedPct=45, waiting=True)

    # Step 3:
    print("Step 3: Driving forward 32.0 cm")
    br.driveForDistance(distance=320, speedPct=80, waiting=True)

    # Step 4:
    print("Step 4: Turning right 18 degrees")
    br.turnInPlace(angle=18, speedPct=45, waiting=True)

    # Step 5:
    print("Step 5: Driving forward 42.0 cm")
    br.driveForDistance(distance=420, speedPct=80, waiting=True)

    # Step 6:
    print("Step 6: Turning left 80 degrees")
    br.turnInPlace(angle=-80, speedPct=45, waiting=True)

    # Step 7:
    print("Step 7: Driving forward 20.0 cm")
    br.driveForDistance(distance=200, speedPct=80, waiting=True)

    # Step 8:
    print("Step 8: Turning left 20 degrees")
    br.turnInPlace(angle=-20, speedPct=45, waiting=True)

    # Step 9:
    print("Step 9: Driving forward 2.0 cm")
    br.driveForDistance(distance=20, speedPct=80, waiting=True)

    # Step 10:
    print("Step 10: Turning left 10 degrees")
    br.turnInPlace(angle=-10, speedPct=45, waiting=True)

    # Step 11:
    print("Step 11: Spinning motor 1500 degrees down")
    br.moveLeftAttachmentMotorForDegrees(degrees=-1500, speedPct=150, waiting=True)

    # Step 12:
    print("Step 12: Spinning motor 1500 degrees down")
    br.moveLeftAttachmentMotorForDegrees(degrees=1500, speedPct=150, waiting=True)

    # Step 13:
    print("Step 13: Driving backward 2.5 cm")
    br.driveForDistance(distance=-25, speedPct=80, waiting=True)

    # Step 14:
    print("Step 14: Turning right 60 degrees")
    br.turnInPlace(angle=60, speedPct=45, waiting=True)

    # Step 15:
    print("Step 15: Driving forward 11.0 cm")
    br.driveForDistance(distance=110, speedPct=80, waiting=True)

    # Step 16:
    print("Step 16: Turning left 85 degrees")
    br.turnInPlace(angle=-85, speedPct=45, waiting=True)

    # Step 17:
    print("Step 17: Driving forward 7.7 cm")
    br.driveForDistance(distance=77, speedPct=80, waiting=True)

    # Step 18:
    print("Step 18: Turning left 85 degrees")
    br.turnInPlace(angle=-85, speedPct=45, waiting=True)

    # Step 19:
    print("Step 19: Driving forward 13.0 cm")
    br.driveForDistance(distance=130, speedPct=80, waiting=True)

    # Step 20:
    print("Step 20: Driving backward 13.0 cm")
    br.driveForDistance(distance=-130, speedPct=80, waiting=True)

    # Step 21:
    print("Step 21: Turning left 40 degrees")
    br.turnInPlace(angle=-40, speedPct=45, waiting=True)

    # Step 22:
    print("Step 22: Driving forward 20.0 cm")
    br.driveForDistance(distance=200, speedPct=80, waiting=True)

    # Step 23:
    print("Step 23: Turning right 45 degrees")
    br.turnInPlace(angle=45, speedPct=45, waiting=True)  # Negative for left turn

    # Step 24:
    print("Step 24: Driving forward 70.0 cm")
    br.driveForDistance(distance=700, speedPct=80, waiting=True)


#

#

#

#

#

# If running this file directly (for testing)
if __name__ == "__main__":
    br = BaseRobot()
    print("Starting custom movement mission...")
    print("Press right button to begin")
    # br.waitForRightButton()
    Run(br)
