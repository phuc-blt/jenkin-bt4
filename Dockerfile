# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

ENV PORT 80

# Expose the port to the outside world
EXPOSE 80
#test
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Run the application
CMD ["/bin/bash", "-c", "python3 main.py"]
