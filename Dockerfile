# Base image with Python
FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ffmpeg && \
    pip install yt-dlp google-cloud-storage && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


# Download and install Google Cloud SDK
RUN curl https://sdk.cloud.google.com | bash
RUN /root/google-cloud-sdk/install --quiet; echo "installed"
ENV PATH="$PATH:/root/google-cloud-sdk/bin"

# Set the working directory
WORKDIR /app

# Copy the script
COPY sun.py /app/sun.py
COPY save_video.sh /app/save_video.sh
COPY gcloud_upload.sh /app

# Set default command to run the script
CMD ["/usr/bin/bash", "/app/gcloud_upload.sh"]
