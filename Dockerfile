# Minimal Dockerfile for Prefect 3.x ML Flow on K8s

FROM python:3.13-bullseye

WORKDIR /app

# Install CA certificates for SSL
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, wheel
RUN python -m pip install --upgrade pip setuptools wheel \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org

# Install Prefect 3.4.17
RUN pip install prefect==3.4.17

# Copy project files
COPY . .

# Default command for local testing (K8s job overrides this)
CMD ["python", "Flow.py"]
