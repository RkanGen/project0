# Dockerfile for Gradio + FastAPI

FROM python:3.9-slim

# Set up working directory
WORKDIR /app

# Copy everything to /app
COPY . /app

# Install dependencies
RUN pip install fastapi uvicorn transformers gradio

# Expose the ports for FastAPI and Gradio
EXPOSE 8000
EXPOSE 7860

# Start both FastAPI and Gradio servers
CMD uvicorn fastapi_app:app --host 0.0.0.0 --port 8000 & python gradio_app.py
