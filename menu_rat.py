#  __  __ _____ _   _ _   _   ____      _  _____
# |  \/  | ____| \ | | | | | |  _ \    / \|_   _|
# | |\/| |  _| |  \| | | | | | |_) |  / _ \ | |
# | |  | | |___| |\  | |_| | |  _ <  / ___ \| |
# |_|  |_|_____|_| \_|\___/  |_| \_\/_/   \_\_|

# To implement, follow this guide:
#
# 1 - Set `br` (your robot instance) to None at the top of your mission file:
#       br = None
#
# 2 - Wrap your mission code in a function called `run(base_robot)`:
#       def run(base_robot):
#           global br  # Tells Python we want to use the br defined at the top
#           br = base_robot  # Links the passed-in robot to br
#
#     Place all your mission code inside this `run` function.
#
# 3 - Add the following code at the end of your file so you can test the mission on its own:
#       if __name__ == "__main__":
#           br = BaseRobot()  # Create a robot instance to test with
#           run(br)           # Run your mission with your test instance
#
# With this setup:
# - You can select and run missions from the main menu.
# - You can test each mission file independently.

from pybricks.tools import hub_menu

from base_robot import *
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Side, Button


# Initialize the robot
br = BaseRobot()

import mission1_2
import missions_05_06_07_back_home
import mission12
import mission3
import missions_9_and_10
import emergency
import mission_east_west

# Dictionary linking menu options to the run functions of each mission
menu_options = {
    "1": missions_9_and_10.run,
    "2": missions_05_06_07_back_home.run,
    "3": mission_east_west.run,
    "4": mission1_2.run,
    "5": mission12.run,
    "6": mission3.run,
    "9": emergency.run,
}

import umath

watch = StopWatch()


def pirat_hub_menu(*menu_items):
    br.hub.display.orientation(up=Side.RIGHT)
    # leftLight = ColorSensor(Port.B)
    # rightLight = ColorSensor(Port.F)
    br.hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])

    current_index = 0  # Start at the first menu item

    while True:
        # Display the current menu item
        br.hub.display.char(menu_items[current_index])

        # Wait for any button to be pressed, and save the result
        pressed = []
        while not any(pressed):
            pressed = br.hub.buttons.pressed()
            wait(10)
            # leftLight.lights.on(100*umath.sin(watch.time()/100))
            # rightLight.lights.on(100*umath.sin(umath.pi+watch.time()/100))

        # Check which button was pressed and update the menu index
        if Button.LEFT in pressed:
            # Move to the previous item, wrap around if at the start
            current_index = (current_index - 1) % len(menu_items)
        elif Button.RIGHT in pressed:
            # Move to the next item, wrap around if at the end
            current_index = (current_index + 1) % len(menu_items)

        # Wait for all buttons to be released before continuing
        while any(br.hub.buttons.pressed()):
            wait(10)

        if Button.CENTER in pressed:
            br.hub.system.set_stop_button(Button.CENTER)
            # leftLight.lights.off()
            # rightLight.lights.off()
            return menu_items[current_index]


# while True:
# Display menu and select an option
# selected = hub_menu('1', '2', '3', '4', '5', '6', '7')
selected = pirat_hub_menu("1", "2", "3", "4", "5", "6", "7", "8", "9")


# Execute the selected program
if selected in menu_options:
    menu_options[selected](br)


else:
    print("Invalid selection.")
