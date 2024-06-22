# Node.js
FROM node:20

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create app directory
WORKDIR /usr/src/app

# Install mockoon-cli globally
RUN npm install -g @mockoon/cli

# Copy application source
COPY . .

# Create a virtual environment
RUN python3 -m venv /usr/src/app/venv

# Activate the virtual environment and install Python dependencies
RUN /usr/src/app/venv/bin/pip install -r /usr/src/app/requirements.txt

# Expose port 3000
EXPOSE 3000

# Command to run mockoon-cli and generate_swagger.py
CMD ["sh", "-c", "/usr/src/app/venv/bin/python /usr/src/app/generate_swagger.py && mockoon-cli start --data /usr/src/app/data/evergreen.json --port 3000"]
