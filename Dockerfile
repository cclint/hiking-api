# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /hiking-api

# Install PostgreSQL and other required packages
RUN apt-get update \
    && apt-get install -y postgresql postgresql-contrib \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /hiking-api

# Install any dependencies
COPY requirements.txt /hiking-api
RUN pip install -r requirements.txt

# Create PostgreSQL database and user
USER postgres
RUN /etc/init.d/postgresql start \
    && psql --command "CREATE USER postgres WITH SUPERUSER PASSWORD 'goldie12';" \
    && createdb -O postgres -E UTF8 -e hiking_trails \
    && /etc/init.d/postgresql stop
USER root

# Create the trails table in the hiking_trails database
RUN /etc/init.d/postgresql start \
    && psql -d hiking_trails -U postgres -a -f /app/init.sql \
    && /etc/init.d/postgresql stop

# Command to run the application when the container starts
CMD ["python", "app.py"]

