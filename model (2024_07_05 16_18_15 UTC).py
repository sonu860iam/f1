# model.py
import torch
from torchvision import models, transforms
from PIL import Image
import requests
from io import BytesIO

# Load pre-trained model
model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Object category names from COCO dataset
COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A',
    'N/A', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana',
    'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut',
    'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table', 'N/A',
    'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book', 'clock',
    'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

# Function to get prediction from image URL
def get_prediction(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")
    transform = transforms.Compose([transforms.ToTensor()])
    img = transform(img)
    with torch.no_grad():
        pred = model([img])
    return pred

from transformers import BertTokenizer, BertForMaskedLM

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model_bert = BertForMaskedLM.from_pretrained('bert-base-uncased')

def generate_description(objects):
    if 'person' in [obj['name'] for obj in objects]:
        return "A person is present in the image."
    return "An image with objects."

def get_image_description(prediction):
    objects = [{'name': COCO_INSTANCE_CATEGORY_NAMES[int(idx)], 
                'bb': {'topLeft': {'x': bbox[0], 'y': bbox[1]}, 'size': {'width': bbox[2]-bbox[0], 'height': bbox[3]-bbox[1]}}}
               for idx, bbox in zip(prediction[0]['labels'].numpy(), prediction[0]['boxes'].detach().numpy())]
    description = generate_description(objects)
    return objects, description
