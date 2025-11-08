# set variable team_name to "pirats"
team_name = "pirats"
# set variable team_number to "34612"
team_number = "34612"
print(team_name)
print(team_number)

for i in range(99):
    print("hip hip horray")


def turn_left(degrees):
    # Add your robot turning logic here
    print(f"Turning left {degrees} degrees")


distance_to_wall = 15  # Example distance in centimeters
if distance_to_wall < 20:  # centimeters
    turn_left(90)
