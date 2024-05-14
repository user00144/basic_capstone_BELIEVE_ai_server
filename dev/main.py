from yolo_inference import inference_detection
from get_sensor_data import get_sensor_data
import time

while(True) :
    time.sleep(0.1)
    humidity, temperature, voicevalue, gasvalue = get_sensor_data()
    detection = inference_detection()
    print(f"sensor data \n humidity : {humidity} , temp = {temperature} , voice = {voicevalue}, gas = {gasvalue}")
    print(f"detection : {detection}")