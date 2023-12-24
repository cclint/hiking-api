# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies
# If you have a requirements.txt file, uncomment the line below
# COPY requirements.txt /app
# RUN pip install -r requirements.txt

# Command to run the application when the container starts
CMD ["python", "trail.py"]
