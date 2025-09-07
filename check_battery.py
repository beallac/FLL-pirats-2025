from pybricks.hubs import PrimeHub

# Initialize the hub
hub = PrimeHub()

# Get the battery voltage in millivolts
battery_voltage = hub.battery.voltage()

# Convert the battery voltage from millivolts to volts
battery_voltage_volts = battery_voltage / 1000
print("Battery voltage (V):", battery_voltage_volts)

# Set the min and max voltage levels for mapping
min_voltage = 6.5  # Voltage for 0% battery
max_voltage = 8.4  # Voltage for 100% battery

# Ensure the voltage is within the expected range to avoid incorrect readings
if battery_voltage_volts > max_voltage:
    battery_voltage_volts = max_voltage
elif battery_voltage_volts < min_voltage:
    battery_voltage_volts = min_voltage

# Map the voltage to a percentage of remaining battery
battery_percentage = (battery_voltage_volts - min_voltage) / (max_voltage - min_voltage) * 100

# Print the estimated battery percentage
print("Battery percentage (%):", round(battery_percentage, 0))