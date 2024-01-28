# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /hiking-api

# Install PostgreSQL and other required packages
# no longer needed

# Copy the current directory contents into the container at /hiking-api
COPY . /hiking-api

# Install any dependencies
COPY requirements.txt /hiking-api
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt -vvv

# Expose port
EXPOSE 5000

# Command to run the application when the container starts
CMD ["python", "app.py"]
