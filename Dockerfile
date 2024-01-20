# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /hiking-api

# Install PostgreSQL and other required packages
RUN apt-get update \
    && apt-get install -y postgresql postgresql-contrib \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /hiking-api
COPY . /hiking-api

# Install any dependencies
COPY requirements.txt /hiking-api
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt -vvv


# Create PostgreSQL database and user if not exists
USER postgres
RUN service postgresql start \
    && if ! psql -t -c '\du' | cut -d \| -f 1 | grep -qw postgres; then \
        psql --command "CREATE USER postgres WITH SUPERUSER PASSWORD 'goldie12';" \
        && createdb -O postgres -E UTF8 -e hiking_trails; \
    fi \
    && service postgresql stop

# Create the hiking_trails database if not exists
RUN service postgresql start \
    && if ! psql -lqt | cut -d \| -f 1 | grep -qw hiking_trails; then \
        createdb -U postgres -O postgres -E UTF8 -e hiking_trails; \
    fi \
    && service postgresql stop

# Create the trails table in the hiking_trails database
RUN service postgresql start \
    && psql -e -d hiking_trails -U postgres -a -f /hiking-api/init.sql

# Expose port
EXPOSE 5000

# Command to run the application when the container starts
CMD ["python", "app.py"]
