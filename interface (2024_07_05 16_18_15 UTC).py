# interface.py
import gradio as gr
from model import get_prediction, get_image_description

def classify(url):
    prediction = get_prediction(url)
    objects, description = get_image_description(prediction)
    return objects, description

iface = gr.Interface(fn=classify, inputs="text", outputs=["json", "text"])
iface.launch()
