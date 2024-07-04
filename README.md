import torch
from torchvision import models, transforms
from PIL import Image
import requests
from io import BytesIO

model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

def get_prediction(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")
    transform = transforms.Compose([transforms.ToTensor()])
    img = transform(img)
    pred = model([img])
    return pred
