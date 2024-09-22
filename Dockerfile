# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Uvicorn if not in requirements.txt
RUN pip install uvicorn

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the application
CMD ["uvicorn", "model_app:app", "--host", "0.0.0.0", "--port", "80"]