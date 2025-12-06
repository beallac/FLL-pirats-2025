from base_robot import *


def Run(br: BaseRobot):
    br.moveLeftAttachmentMotorForDegrees(degrees=595, speedPct=60)
    br.driveForDistance


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
