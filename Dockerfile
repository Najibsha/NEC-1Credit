# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy necessary files
COPY personal-api.py /app/

# Install dependencies
RUN pip install flask

# Expose the port
EXPOSE 5000

# Run the API
CMD ["python", "personal-api.py"]
