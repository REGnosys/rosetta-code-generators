# Use an official Python image as the base image
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /pygen

# Copy the current directory contents into the container at /pygen
COPY build /pygen
RUN ls -la /pygen/*

# Make the script executable
RUN chmod +x /pygen/build.sh
RUN chmod +x /pygen/pytests.sh

# Define the command to run the application
ENTRYPOINT ["/bin/sh", "-c"]
CMD ["/pygen/build.sh && /pygen/pytests.sh"]
