# Use an official Python runtime as the base image
FROM python:3.10.14-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8501 to run Streamlit
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]
