# Sử dụng image Python chính thức làm base image
FROM python:3.9-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Copy requirements.txt vào container và cài đặt các dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . /app/

# Cài đặt FastAPI và Uvicorn (nếu chưa cài đặt trong requirements.txt)
RUN pip install fastapi uvicorn

# Mở cổng 80 cho container
EXPOSE 80

# Khởi động ứng dụng FastAPI bằng uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
