FROM python:3.11-slim

# install dependencies
RUN apt-get update && \
    apt-get install -y wget gnupg2 --no-install-recommends

# Install Chrome
RUN wget -O- https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome-keyring.gpg] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# verify installation
RUN python --version && google-chrome --version

# Copy project files
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV CHROME_NO_SANDBOX=1


#CMD ["bash"]
CMD ["python", "local_login.py"]
