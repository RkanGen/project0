from fastapi import FastAPI, HTTPException
from transformers import pipeline

app = FastAPI()

# Example: Load a LLaMA 2 model using the pipeline
text_generator = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI ML model service!"}

@app.post("/generate/")
def generate(text: str):
    try:
        result = text_generator(text, max_length=100)
        generated_text = result[0]["generated_text"]
        return {"generated_text": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
