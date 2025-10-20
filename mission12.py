from base_robot import *


# Custom Movement Mission:
# - Drive forward 53.1 cm (531 mm)
# - Turn 90 degrees left
# - Drive forward 2.5 cm (25 mm)
# - Drive forward 14.3 cm (143 mm)
#
# Robot Alignment: Place robot at desired starting position
# No special arm positions or attachments needed

br = None


def run(base_robot):
    global br
    br = base_robot

    br.driveForDistance(475)
    br.driveForDistance(-475)
    br.moveLeftAttachmentMotorForMillis(millis=1500)
    br.turnInPlace(-90)
    br.driveForDistance(90)
    br.turnInPlace(90)
    br.driveForDistance(750)
    br.driveForDistance(-750)
    br.moveLeftAttachmentMotorForMillis(millis=1575, speedPct=-80)


if __name__ == "__main__":
    br = BaseRobot()
    run(br)
