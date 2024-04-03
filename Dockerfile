
# Use an official Python runtime as the base image
FROM python:3.10-bookworm

# Set the working directory in the container
WORKDIR /app

# Install pip
RUN python -m ensurepip --upgrade

# Copy your Python script and requirements.txt file into the container
COPY app.py .
COPY requirements.txt .

# Install the Python packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run your Python script when the container starts
CMD ["python", "app.py"]