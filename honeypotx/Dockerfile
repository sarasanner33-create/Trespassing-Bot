FROM python:3.11-slim-bookworm

RUN useradd -ms /bin/bash honeypotuser
USER honeypotuser
WORKDIR /home/honeypotuser

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

COPY --chown=honeypotuser:honeypotuser . .

EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
