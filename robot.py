# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "http://localhost:3000/robot_statuses"

status_data  = '''{"robot_id": "3f54b65a-675b-11ec-a68d-0242ac110002",
                 "status_time": "2021-12-27T22:30:09.176+00:00",
                "status_location": {
                        "type": "Point",
                        "coordinates": [
                                50.7373,
                                3.075
                                ]
                                }
                }
                '''

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = status_data)

# extracting response text
pastebin_url = r.text
print("The robot response is:%s"%pastebin_url)
