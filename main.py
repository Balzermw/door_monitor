import time

# Importing our modules
from settings import Constants
from door_sensor import DoorSensor

# Entry Point
def main():
    # Door Sensor Object (Deals with API and stores the door status)
    door_sensor = DoorSensor(Constants.group_id, Constants.door_sensor_id)

    interval = 15  # Seconds

    while True:
        print(door_sensor.sense())
        time.sleep(interval)

# If the file is being executed as main file (i.e: not being used as a module)
if __name__ == "__main__":
    main()