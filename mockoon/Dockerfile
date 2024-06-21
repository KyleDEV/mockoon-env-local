# Node.js
FROM node:20

# Create app directory
WORKDIR /usr/src/app

# Install mockoon-cli globally
RUN npm install -g @mockoon/cli

# Copy Mockoon the API evironment file (data/evergreen.json to the app directory)
COPY data/evergreen.json /usr/src/app/data/evergreen.json

# Expose port 3000
EXPOSE 3000

# Command to run mockoon-cli
CMD ["mockoon-cli", "start", "--data", "/usr/src/app/data/evergreen.json", "--port", "3000"]
