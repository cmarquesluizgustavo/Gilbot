FROM python:latest

# Install dependencies
RUN apt-get -y update && apt-get install -y \
    ffmpeg

# Upgrade pip
RUN pip install --upgrade pip

# Set the workdir as app for relative paths
WORKDIR /app

# Copy requirements into app 
# just this file first to cache the pip install step when code changes
COPY requirements.txt .

# Install python requirements 
RUN pip install -r requirements.txt

COPY . .

ENV bot_token None

CMD [ "python3", "main.py" ]