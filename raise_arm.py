from base_robot import *

# Set br to None at the top (required for menu structure)
br = None


def run(base_robot):
    """Mission 05-06-07 West - Main mission function"""
    global br  # Tells Python we want to use the br defined at the top
    br = base_robot  # Links the passed-in robot to br

    br.moveLeftAttachmentMotorForDegrees(degrees=900, speedPct=80)


if __name__ == "__main__":
    br = BaseRobot()  # Create a robot instance to test with
    run(br)  # Run your mission with your test instance
