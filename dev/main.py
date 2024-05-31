from yolo_inference import inference_detection
from get_sensor_data import get_sensor_data
import time
import requests
import json

url = 'http://192.168.0.37:8080'
headers = {'Content-Type': 'application/json'}


def detect(detection):
    if not detection:
        return 1

    if 0 in detection:
        return 0
    else:
        return 1


while (True):
    time.sleep(1)
    humidity, temperature, voicevalue, gasvalue = get_sensor_data()
    detection = detect(inference_detection())
    data = {'helmet': detection, 'temperature': temperature, 'sound': voicevalue, 'gas': gasvalue}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response)
    print(response.headers)









