from base_robot import *


br = None


def run(br: BaseRobot):
    """
    Execute the custom movement sequence

    Args:
        br (BaseRobot): The robot instance to control
    """

    br.moveLeftAttachmentMotorForDegrees(degrees=170, speedPct=150, waiting=True)
    br.driveForDistance(distance=25, speedPct=80, waiting=True)
    br.turnInPlace(angle=-32.5, speedPct=45, waiting=True)
    br.driveForDistance(distance=250, speedPct=80, waiting=True)
    br.turnInPlace(angle=-20, speedPct=45, waiting=True)
    br.turnInPlace(angle=25, speedPct=45, waiting=True)
    br.driveForDistance(distance=100, speedPct=80, waiting=True)
    br.turnInPlace(angle=26.4, speedPct=45, waiting=True)
    br.moveLeftAttachmentMotorForDegrees(degrees=1100, speedPct=150, waiting=True)
    br.driveForDistance(distance=460, speedPct=80, waiting=True)
    br.turnInPlace(angle=-90, speedPct=45, waiting=True)
    br.driveForDistance(distance=180, speedPct=80, waiting=True)
    br.turnInPlace(angle=-20, speedPct=45, waiting=True)
    br.moveLeftAttachmentMotorForDegrees(degrees=-1500, speedPct=150, waiting=True)
    br.moveLeftAttachmentMotorForDegrees(degrees=1500, speedPct=150, waiting=True)
    br.driveForDistance(distance=-25, speedPct=80, waiting=True)
    br.turnInPlace(angle=60, speedPct=45, waiting=True)
    br.driveForDistance(distance=110, speedPct=80, waiting=True)
    br.turnInPlace(angle=-85, speedPct=45, waiting=True)
    br.driveForDistance(distance=80, speedPct=80, waiting=True)
    br.turnInPlace(angle=-85, speedPct=45, waiting=True)
    br.driveForDistance(distance=130, speedPct=80, waiting=True)
    br.driveForDistance(distance=-130, speedPct=80, waiting=True)
    br.turnInPlace(angle=-40, speedPct=45, waiting=True)
    br.driveForDistance(distance=200, speedPct=80, waiting=True)
    br.turnInPlace(angle=45, speedPct=45, waiting=True)  # Negative for left turn
    br.driveForDistance(distance=700, speedPct=80, waiting=True)
    br.moveLeftAttachmentMotorForDegrees(degrees=-1270, speedPct=150, waiting=True)

    # =============================================== #
    #  ._.  ._._____._.   ._.    ._____.              #
    #  | |  | | ____| |   | |    /  _  \              #
    #  | |--| | ._| | |   | |   |  | |  |             #
    #  | |--| | |___| |___| |___|  |_|  |             #
    #  |_|  |_|_____\_____\______\_____/              #
    #                                                 #
    #  ._______._.  ._._____.____.._____.             #
    #  |__. .__| |  | | ____|  _ \| ____|             #
    #     | |  | |--| |  _| | |_) |  _|               #
    #     | |  | |--| | |___|  _ <| |___. .__.        #
    #     |_|  |_|  |_|_____|_| |_|_____|  \ \        #
    #                                      /_|        #
    #  ._________.    .____.    ._.._____.______.._.  #
    #  |_. ._. ._|    | ._.\    / \|_   _| .____|| |  #
    #    | | | |      | |_) |  / _ \ | | | |____ |_|  #
    #    | | | |_.    |  _ <  / ___ \| | |____  |._.  #
    #    |_|  \__|    |_| \_\/_/   \_\_| |______||_|  #
    #                                                 #
    # =============================================== #


# If running this file directly (for testing)
if __name__ == "__main__":
    br = BaseRobot()
    print("Starting custom movement mission...")
    print("Press right button to begin")
    # br.waitForRightButton()
    run(br)
