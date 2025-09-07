from base_robot import *

"""
SAFE WHEEL CLEANING

Spin the drive wheels in the air to remove dust/debris. DO NOT run this
on the table. Lift the robot so the wheels are off the mat before starting.

Usage: run this file on the hub. It will spin both wheels forward, then
reverse, at moderate speed for a few seconds each.
"""


def Run(br: BaseRobot):
    # Moderate speed in deg/sec for direct motor control
    speed = 600

    # Spin forward
    br.leftDriveMotor.run_time(speed=speed, time=3000, wait=False)
    br.rightDriveMotor.run_time(speed=speed, time=3000, wait=True)
    br.waitForMillis(500)

    # Spin reverse
    br.leftDriveMotor.run_time(speed=-speed, time=3000, wait=False)
    br.rightDriveMotor.run_time(speed=-speed, time=3000, wait=True)
    br.waitForMillis(250)

    # Beep to indicate done
    br.hub.speaker.beep(frequency=1000, duration=400)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
