FROM python:3.10-slim

# Install dependencies
RUN pip install python-dotenv langchain gigachain

# Copy your modules and environment file
COPY . .

# Set environment variables from dotenv file
ENV $(cat .env | xargs)

# Define the entrypoint and command
CMD ["python", "main.py"]
