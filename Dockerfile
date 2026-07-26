FROM python:3.11-slim
# Start with Linux + Python 3.11

WORKDIR /app
# Create working location /app

COPY requirements.txt .
# Copy dependencies

RUN pip install \
    --no-cache-dir \
    -r requirements.txt
# Install requiements

COPY . .
# app.py loan_model.py api.py models/

RUN chmod +x start.sh

EXPOSE 8501 8000

CMD ["./start.sh"]
