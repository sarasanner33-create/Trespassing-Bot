FROM python:3.11-slim-bookworm

# Install security utilities and process management tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    util-linux \
    && rm -rf /var/lib/apt/lists/*

# Create non-root runner user
RUN useradd -ms /bin/bash sandboxuser
USER sandboxuser
WORKDIR /home/sandboxuser

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

COPY --chown=sandboxuser:sandboxuser . .

CMD ["python3", "runner.py"]
