from base_robot import *

# Import included sample missions so this launcher works in a fresh repo
import sample_mission
import basic_drive_mission
import motor_test
import measure_path as measure_path
import clean_wheels


br: BaseRobot = BaseRobot()

pressed: list[Button] = []
col: Color = br.colorSensor.color()

# Map detected color to a mission module
mission_map = {
    Color.SENSOR_YELLOW: sample_mission,  # type: ignore
    Color.SENSOR_GREEN: basic_drive_mission,  # type: ignore
    Color.SENSOR_BLUE: motor_test,  # type: ignore
    Color.SENSOR_WHITE: measure_path,  # type: ignore
    Color.SENSOR_ORANGE: clean_wheels,  # type: ignore
}

while True:
    # Wait for a color and left button to launch
    while True:
        col = br.colorSensor.color()
        if col == Color.SENSOR_NONE:
            br.hub.display.icon(Icon.SAD)
            br.hub.light.on(Color.RED)
        else:
            br.hub.display.icon(Icon.HAPPY)
            br.hub.light.on(br.myColor2DefaultColorDict.get(col, Color.WHITE))

        wait(50)
        pressed = br.hub.buttons.pressed()
        if Button.LEFT in pressed:
            break
        if Button.BLUETOOTH in pressed:
            # Quick clean: spin wheels at high speed for a brief time
            br.driveForMillis(millis=3000, speedPct=100, gyro=False)

    # Launch mapped mission if available
    mod = mission_map.get(col)
    if mod and hasattr(mod, "Run"):
        print("Launching", mod.__name__)
        mod.Run(br)  # type: ignore
    else:
        print("No mission mapped to this color. Holding.")
        br.hub.speaker.beep(400, 250)

