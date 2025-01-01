from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Định nghĩa lớp yêu cầu đầu vào cho /check_prime
class PrimeRequest(BaseModel):
    number: int

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/check_prime")
async def check_prime(request: PrimeRequest):
    number = request.number
    # Kiểm tra số âm hoặc không hợp lệ
    if number <= 1:
        return {"is_prime": False}
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return {"is_prime": False}
    return {"is_prime": True}

@app.get("/get_version")
def get_version():
    return {"version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
