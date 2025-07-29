FROM python:3.11-slim

# install dependencies
RUN apt-get update && \
    apt-get install -y wget gnupg2 curl dirmngr --no-install-recommends

# Install Chrome
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Microsoft Edge
RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | gpg --dearmor > /usr/share/keyrings/microsoft-edge.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-edge.gpg] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge.list && \
    apt-get update && \
    apt-get install -y microsoft-edge-stable --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# verify installation
RUN python --version && google-chrome --version && microsoft-edge --version

# Copy project files
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV CHROME_NO_SANDBOX=1


#CMD ["bash"]
CMD ["python", "local_login.py"]
