from torchvision import transforms
from PIL import Image
import numpy as np
import torch
import cv2

capture_device = 0
cap = cv2.VideoCapture(capture_device)


def initialize_cap():
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FPS, 24)


initialize_cap()

model_name = './custom_model.pt'
model = torch.hub.load("WongKinYiu/yolov7", 'custom', model_name)

model.eval()


def read_img():
    ret, image = cap.read()
    if image is not None:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image


def get_prediction(image):
    predicted_classes = []
    if image is not None:
        results = model(image, size=640)
        results.save('pred')
        # x1 | y1 | x2 | y2 | conf | detclass
        pred = results.pred
        for r in pred:
            r_ = r.tolist()
            for i in r_:
                predicted_classes.append(i[5])
    return predicted_classes


def inference_detection():
    img = read_img()
    classes = get_prediction(img)
    det = [1, 2]
    return classes
