# Sử dụng image Python chính thức
FROM python:3.9-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài đặt các thư viện cần thiết
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn vào container
COPY . /app

# Cấu hình port mà FastAPI sẽ chạy
EXPOSE 80

# Lệnh để chạy ứng dụng FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
