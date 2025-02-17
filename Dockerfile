# Use official Python image
FROM python:3.8

# Set working directory inside the container
WORKDIR /app

# Copy necessary files
COPY requirements.txt .
COPY models/model.pkl models/model.pkl
COPY src/app.py src/app.py

# Install dependencies
RUN pip install -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
