FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential git curl mecab libmecab-dev mecab-ipadic-utf8 sudo


# Install Python dependencies
RUN pip install --upgrade pip

COPY  requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . .

# Default command
CMD ["bash"]
