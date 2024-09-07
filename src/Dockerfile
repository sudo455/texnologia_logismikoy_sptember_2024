# official python image
FROM python:3.12.5-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apk upgrade
# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 80

# Healthcheck for docker and portainer use to see if all is ok 
HEALTHCHECK CMD curl --fail http://localhost:80/_stcore/health

# Run app.py when the container launches
CMD ["streamlit", "run", "main.py", "--server.port=80", "--server.address=0.0.0.0", "--server.maxUploadSize=512", "--client.toolbarMode=minimal" ]
