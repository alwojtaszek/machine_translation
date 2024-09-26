FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run the Streamlit application
CMD ["streamlit", "run", "translator_app.py"]