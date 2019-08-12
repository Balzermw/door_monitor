import json
import requests

from datetime import datetime

from settings import Constants

class DoorSensor():

    # Constructor
    def __init__(self, group_id, sensor_id):
        self.sensor_id = sensor_id  # ID of the sensor (used in API Request)
        self.group_id = group_id  # Group ID of the sensor (used in API Request)
        self.name = ""  # Name of the sensor (Retrieved from the API Response)
        self.vehicleId = ""  # ID of the vehicle (Retrieved from the API Response)
        self.doorClosed = False  # Boolean denoting the status of door
        self.doorStatusTime = ""  # The time that at which the status was recorded

    def sense(self):
        # POST Request's Body
        body = {
            "groupId": self.group_id,
            "sensors": [self.sensor_id]
        }

        # Request's Query Parameter (appended to URL after ?)
        params = {
            "access_token": Constants.access_token
        }

        # Sending a POST request to the temperature API URL/Endpoint
        response = requests.post(Constants.door_api_endpoint, params=params, json=body)

        # If response status code is not 200 OK, something is wrong, so raise exception
        if response.status_code != 200:
            raise Exception("Non OK Response from Server. Response:\n" + response.text)
        
        # Parse response as json (to dictionary)
        response = response.json()
        
        # Extract data from dictionary and set it as object's properties
        sensor_data = response["sensors"][0]

        self.name = sensor_data["name"]
        self.vehicleId = sensor_data["vehicleId"]

        time = datetime.strptime(sensor_data["doorStatusTime"], Constants.api_time_format)
        self.doorStatusTime = time.strftime("%d-%b-%y %H:%M")
        
        self.doorClosed = sensor_data["doorClosed"]

        status = "closed" if self.doorClosed else "open"

        return F"The door is {status} @ {self.doorStatusTime}"