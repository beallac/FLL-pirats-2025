from base_robot import *

# Move the robot forward 10 cm (100 mm)
if __name__ == "__main__":
    br = BaseRobot()
    br.driveForDistance(distance=100, speedPct=80, then=Stop.BRAKE, waiting=True)
