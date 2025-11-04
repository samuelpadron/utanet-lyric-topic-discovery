FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y git curl mecab libmecab-dev mecab-ipadic-utf8 sudo

# Install Python dependencies
COPY  requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["bash"]
