# Use an official Python runtime as a parent image
# 3.9-slim is a lightweight version of Python 3.9, good for minimizing image size.
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir keeps the image smaller by not caching the packages.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Define environment variable PORT
# This sets a default, but it can be overridden at runtime.
ENV PORT=3000

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run app.py when the container launches
CMD ["python", "app.py"]
