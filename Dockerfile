# Use the official Python 3.11 slim image based on Debian Bookworm
FROM python:3.11-slim-bookworm

# Set working directory inside container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Asia/Tashkent \
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

# Install system dependencies and clean up cache to reduce image size
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    libpq-dev \
    gcc \
    gettext \
    curl \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# Copy entrypoint script and make it executable
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

RUN python app/collect_static.py

# Create non-root user
RUN adduser --disabled-password --no-create-home appuser
USER appuser

EXPOSE 9090

# Healthcheck on /health endpoint on port 9090
HEALTHCHECK --interval=10s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:9090/health || exit 1

# Entrypoint and default command to run app
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "app/main.py"]

