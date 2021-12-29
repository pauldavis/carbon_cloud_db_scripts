from datetime import datetime
import pytz
import json
import random

# importing the requests library
import requests

# import concurrent libray to increase speed
from concurrent.futures import ThreadPoolExecutor


# parameters
readings_per_burst = 10
metric_value_max = 10
start_point = [-107.834117870184, 31.789303379317]
end_point = [-107.824923914706,31.791937418138]


# defining the api-endpoint
api_endpoint = "http://localhost:3000/robot_statuses"

robot_status_dict = {}

status_location = {}
status_location["type"] = "Point"

horizontal_distance = end_point[0] - start_point[0]
vertical_distance = end_point[1] - start_point[1]

horizontal_increment = horizontal_distance/readings_per_burst
vertical_increment = vertical_distance/readings_per_burst

robot_status_dict['status_location'] = status_location

robot_status_dict['robot_id'] = '3f54b65a-675b-11ec-a68d-0242ac110002'

def send_metric(reading_number):

    robot_status_dict['status_time'] = str(datetime.now(tz=pytz.UTC))
    robot_status_dict['status_data'] = random.randint(0, metric_value_max)

    reading_location = [0,0]
    reading_location[0] = start_point[0] + reading_number * horizontal_increment
    reading_location[1] = start_point[1] + reading_number * vertical_increment

    status_location["coordinates"] = reading_location

    robot_status_dict['status_location'] = status_location

    robot_status_json = json.dumps(robot_status_dict)

    # sending post request and saving response as response object
    # print(status_location["coordinates"])
    requests.post(url=api_endpoint, data=robot_status_json)

    # extracting response text
#    cloud_response = r.text
#    print("The cloud response is:%s" % cloud_response)


processes = []

with ThreadPoolExecutor(max_workers=16) as executor:
    for i in range(readings_per_burst):
        processes.append(executor.submit(send_metric(i)))
print("Done")

