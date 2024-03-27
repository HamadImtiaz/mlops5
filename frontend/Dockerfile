FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the frontend application files into the container
COPY . /usr/src/app

EXPOSE 5001

# Install Flask and other dependencies
RUN pip install --no-cache-dir Flask Flask-PyMongo

# Define the command to run the Flask application
CMD ["python", "app.py"]
