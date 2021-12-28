from datetime import datetime
import pytz
import json
import random

# importing the requests library
import requests

# import concurrent libray to increase speed
from concurrent.futures import ThreadPoolExecutor


# parameters
posts_per_burst = 10000
metric_value_max = 10

# defining the api-endpoint
api_endpoint = "http://localhost:3000/robot_statuses"

robot_status_dict = {}

status_location = {}
status_location["type"] = "Point"
status_location["coordinates"] = [-107.834117870184429, 31.791937418137536]
robot_status_dict['status_location'] = status_location

robot_status_dict['robot_id'] = '3f54b65a-675b-11ec-a68d-0242ac110002'

def send_metric():

    robot_status_dict['status_time'] = str(datetime.now(tz=pytz.UTC))
    robot_status_dict['status_data'] = random.randint(0, metric_value_max)

    robot_status_json = json.dumps(robot_status_dict)

    # sending post request and saving response as response object
    r = requests.post(url=api_endpoint, data=robot_status_json)

    # extracting response text
    cloud_response = r.text
    print(i)
    print("The cloud response is:%s" % cloud_response)

processes = []

with ThreadPoolExecutor(max_workers=8) as executor:
    for i in range(posts_per_burst):
        processes.append(executor.submit(send_metric))

