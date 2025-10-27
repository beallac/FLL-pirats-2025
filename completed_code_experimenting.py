from base_robot import *

# Set br to None at the top (required for menu structure)
br = None


def run(base_robot):
    """Mission 05-06-07 West - Main mission function"""
    global br  # Tells Python we want to use the br defined at the top
    br = base_robot  # Links the passed-in robot to br

    # Leave starting point; drive 11 cm
    br.driveForDistance(distance=110, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn to mission 09; turn -34 degrees
    br.turnInPlace(angle=-34, speedPct=80, waiting=True)
    # Drive to mission 09; drive 36.5 cm
    br.driveForDistance(distance=365, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn to missions 05-07; turn 70 degrees
    br.turnInPlace(angle=70, speedPct=80, waiting=True)
    # Drive to missions 05-07; drive 14.2 cm
    br.driveForDistance(distance=142, speedPct=80, then=Stop.BRAKE, waiting=True)

    # Lower claw by 922 degrees
    br.moveLeftAttachmentMotorForDegrees(degrees=-922, speedPct=80)

    # Release ores (complete mission 06); turn -20 degrees
    br.turnInPlace(angle=-20, speedPct=80, waiting=True)

    # Approach mission 05; drive 4.6 cm
    br.driveForDistance(distance=46, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Flip structure upright (complete mission 05); turn -38 degrees
    br.turnInPlace(angle=-38, speedPct=60, waiting=True)
    # Raise claw by 940 degrees, avoiding making contact with any objects
    br.moveLeftAttachmentMotorForDegrees(degrees=940, speedPct=60)
    # Turn to slight side of mission 07; turn 30 degrees
    br.turnInPlace(angle=30, speedPct=60, waiting=True)
    # Approach side of mission 07; drive 11 cm
    br.driveForDistance(distance=110, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn to mission 07; turn 24 degrees
    br.turnInPlace(angle=24, speedPct=60, waiting=True)
    # Lower claw by 940 degrees, getting the claw in position
    br.moveLeftAttachmentMotorForDegrees(degrees=-940, speedPct=120)
    # Slot the claw through mission 07; drive 4 cm
    br.driveForDistance(distance=40, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Retrive millstone (complete mission 07); turn 44 degrees
    br.turnInPlace(angle=44, speedPct=80, waiting=True)
    # Start driving west
    # Raise claw by 900 degrees, avoiding making contact with any objects
    br.moveLeftAttachmentMotorForDegrees(degrees=900, speedPct=60)
    # Drive to mission 09; drive -17.2 cm
    br.driveForDistance(distance=-172, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn towards left of mission 05; turn -128 degrees
    br.turnInPlace(angle=-128, speedPct=80, waiting=True)
    # Drive towards left of mission 05; drive 12.8 cm
    br.driveForDistance(distance=128, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn towards west end of board; turn -42.6 degrees
    br.turnInPlace(angle=-42.6, speedPct=80, waiting=True)
    # Drive to west end of board, right before mission 01; drive 121.6 cm
    br.driveForDistance(distance=1216, speedPct=80, then=Stop.BRAKE, waiting=True)
    # Turn to home area; turn -90 degrees
    br.turnInPlace(angle=-90, speedPct=80, waiting=True)  # Drive into home area
    br.driveForDistance(distance=628, speedPct=80, then=Stop.BRAKE, waiting=True)


if __name__ == "__main__":
    br = BaseRobot()  # Create a robot instance to test with
    run(br)  # Run your mission with your test instance
