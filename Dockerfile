# Use a Python 3.10 base image
FROM python:3.10.14-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container
COPY . /app/

# Set environment variable to disable Streamlit's warning messages
ENV STREAMLIT_SERVER_HEADLESS=true

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run your app using Streamlit
CMD ["streamlit", "run", "app.py"]
