from base_robot import *

# Set br to None at the top (required for menu structure)
br = None


def run(base_robot):
    """Combined Maze Code - Main mission function"""
    global br  # Tells Python we want to use the br defined at the top
    br = base_robot  # Links the passed-in robot to br

    # Maze navigation script
    # Sequence:
    # 1. Drive 11 cm
    # 2. Turn -34 degrees
    # 3. Drive 36 cm
    # 4. Turn 65 degrees
    # 5. Drive 14 cm
    # 6. Lower arm by 980 degrees
    # 6. Turn -22.5 degrees
    # 7. Drive 4 cm
    # 8. Turn -25 degrees
    # 9. Turn 21 degrees
    # 10. Raise arm by 640 degrees
    # 11. Drive 11 cm
    # 12. Turn 24 degrees
    # 13. Drive 7.25 cm
    # 14. Lower arm by 640 degrees
    # 15. Drive 10 cm
    # 16. Turn 44 degrees
    # 17. Raise arm by 980 degrees
    # 18. Drive backwards 3.5 cm
    # 19. Turn 136 degrees
    # 20. Drive 15 cm
    # 21. Turn -65 degrees
    # 22. Drive 42 cm
    # 23. Turn 215 degrees
    # 24. Drive backwards 17.5 cm

    br.driveForDistance(
        distance=110, speedPct=80, then=Stop.BRAKE, waiting=True
    )  # 11 cm
    br.turnInPlace(angle=-34, speedPct=50, waiting=True)  # -34 degrees
    br.driveForDistance(
        distance=360, speedPct=80, then=Stop.BRAKE, waiting=True
    )  # 36 cm
    br.turnInPlace(angle=65, speedPct=50, waiting=True)  # 65 degrees
    br.driveForDistance(
        distance=140, speedPct=80, then=Stop.BRAKE, waiting=True
    )  # 14 cm

    br.moveLeftAttachmentMotorForDegrees(degrees=-980, speedPct=50)  # Lower arm

    br.turnInPlace(angle=-22.5, speedPct=50, waiting=True)  # -22.5 degrees

    # Drive forward 4 cm and turn -25 degrees
    br.driveForDistance(distance=40.0, speedPct=80, then=Stop.BRAKE, waiting=True)
    br.turnInPlace(angle=-25, speedPct=50, waiting=True)
    # Turn 21 degrees
    br.turnInPlace(angle=21, speedPct=50, waiting=True)
    # Raise arm by 640 degrees
    br.moveLeftAttachmentMotorForDegrees(degrees=640, speedPct=50)
    # Drive 11 cm (110 mm)
    br.driveForDistance(distance=110, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn 24 degrees
    br.turnInPlace(angle=24, speedPct=50, waiting=True)
    # Lower arm by 640 degrees
    br.moveLeftAttachmentMotorForDegrees(degrees=-640, speedPct=50)
    br.driveForDistance(distance=40, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn 44 degrees
    br.turnInPlace(angle=44, speedPct=20, waiting=True)
    # Raise arm by 980 degrees
    br.moveLeftAttachmentMotorForDegrees(degrees=980, speedPct=50)
    # Drive backwards 3.5 cm
    br.driveForDistance(distance=-35, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn 136 degrees
    br.turnInPlace(angle=136, speedPct=50, waiting=True)
    # Drive 15 cm
    br.driveForDistance(distance=150, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn -65 degrees
    br.turnInPlace(angle=-65, speedPct=50, waiting=True)
    # Drive 42 cm
    br.driveForDistance(distance=420, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn 215 degrees
    br.turnInPlace(angle=215, speedPct=50, waiting=True)
    # Drive backwards 17.5 cm
    br.driveForDistance(distance=-175, speedPct=80, then=Stop.BRAKE, waiting=True)


if __name__ == "__main__":
    br = BaseRobot()  # Create a robot instance to test with
    run(br)  # Run your mission with your test instance
