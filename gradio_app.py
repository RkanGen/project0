# gradio_app.py

import gradio as gr
import requests

# Define a function to call the FastAPI backend
def classify_text(text):
    response = requests.post("http://127.0.0.1:8000/predict/", json={"text": text})
    if response.status_code == 200:
        result = response.json()
        return f"Prediction: {result['prediction']}, Confidence: {result['score']:.2f}"
    else:
        return "Error: Something went wrong with the prediction."

# Create the Gradio interface
iface = gr.Interface(
    fn=classify_text,
    inputs="text",
    outputs="text",
    title="Text Classification with FastAPI"
)

iface.launch()
