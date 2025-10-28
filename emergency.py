from base_robot import *


def run(base_robot):
    global br
    br = base_robot
    br.driveForDistance(distance=1200)

    br.turnInPlace(angle=-30)
    br.driveForDistance(distance=700)


if __name__ == "__main__":
    br = BaseRobot()
    run(br)
