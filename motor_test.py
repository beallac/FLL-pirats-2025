# MOTOR TEST SCRIPT
# This utility script tests each motor individually to verify they are working properly.
# 
# WHAT IT DOES:
# - Tests each motor one at a time for 2 seconds each
# - Tests motors in sequence: left drive, front attachment, right drive, rear attachment
# - Uses moderate speed (50%) for safe testing
# - Provides hub display feedback showing which motor is being tested
#
# HOW TO USE:
# 1. Place robot in a safe area with room to move
# 2. Ensure all motors and attachments can move freely
# 3. Run this script on the robot
# 4. Watch each motor move for 2 seconds in sequence
# 5. Check that all motors respond correctly
#
# USEFUL FOR:
# - Verifying motor connections and port assignments
# - Checking motor direction and operation
# - Troubleshooting mechanical issues
# - Testing after robot assembly or modifications
#
# SAFETY: Motors run at 50% speed for controlled testing

from base_robot import *


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Test 1: Left Drive Motor (Port A)
    print("Testing Left Drive Motor (Port A) for 2 seconds...")
    br.leftDriveMotor.run_time(speed=500, time=2000, wait=True)  # 50% speed for 2 seconds
    br.waitForMillis(500)  # Brief pause between tests

    # Test 2: Front Attachment Motor (Port D)
    print("Testing Front Attachment Motor (Port D) for 2 seconds...")
    br.moveLeftAttachmentMotorForMillis(millis=2000, speedPct=50, waiting=True)
    br.waitForMillis(500)  # Brief pause between tests
    
    # Test 3: Right Drive Motor (Port E)
    print("Testing Right Drive Motor (Port E) for 2 seconds...")
    br.rightDriveMotor.run_time(speed=500, time=2000, wait=True)  # 50% speed for 2 seconds
    br.waitForMillis(500)  # Brief pause between tests
    
    # Test 4: Rear Attachment Motor (Port C)
    print("Testing Rear Attachment Motor (Port C) for 2 seconds...")
    br.moveRightAttachmentMotorForMillis(millis=2000, speedPct=50, waiting=True)
    
    # Test complete
    print("Motor test complete!")
    br.hub.speaker.beep(frequency=1000, duration=500)  # Success beep


# Leave everything below here and don't type anything below this line
# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
