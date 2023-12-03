# Use a base image
FROM node:18

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json /app/

# Install dependencies
RUN npm install

# Copy the application code
COPY . /app/

# Expose the application port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
