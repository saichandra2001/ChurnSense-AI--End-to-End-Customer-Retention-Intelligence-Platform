# Base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy everything
COPY . /app

#Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Expose port (FastAPI default)
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]