from base_robot import *

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
# 11. Drive 4 cm
# 12. Turn 24 degrees
# 13. Drive 7.25 cm
# 14. Lower arm by 640 degrees
# 16. Turn 44 degrees

if __name__ == "__main__":
    br = BaseRobot()
    # Drive 11 cm
    br.driveForDistance(distance=110, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn -34 degrees
    br.turnInPlace(angle=-34, speedPct=50, waiting=True)
    # Drive 36 cm
    br.driveForDistance(distance=360, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn 65 degrees
    br.turnInPlace(angle=65, speedPct=50, waiting=True)
    # Drive 14 cm
    br.driveForDistance(distance=140, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Lower arm by 980 degrees
    br.moveLeftAttachmentMotorForDegrees(degrees=-980, speedPct=50)
    # Turn -22.5 degrees
    br.turnInPlace(angle=-22.5, speedPct=50, waiting=True)

    # Drive 4 cm
    # Turn -25 degrees
    br.driveForDistance(distance=40.0, speedPct=80, then=Stop.BRAKE, waiting=True)
    br.turnInPlace(angle=-25, speedPct=50, waiting=True)
    # Turn 21 degrees
    br.turnInPlace(angle=21, speedPct=50, waiting=True)
    # Raise arm by 640 degrees
    # Drive 4 cm
    br.moveLeftAttachmentMotorForDegrees(degrees=640, speedPct=50)
    br.driveForDistance(distance=40, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn 24 degrees
    br.turnInPlace(angle=24, speedPct=50, waiting=True)
    # Drive 7.25 cm
    br.driveForDistance(distance=72.5, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Lower arm by 640 degrees
    br.driveForDistance(distance=100, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn 44 degrees
    br.turnInPlace(angle=44, speedPct=50, waiting=True)
    # Raise arm by 980 degrees
    br.moveLeftAttachmentMotorForDegrees(degrees=980, speedPct=50)
