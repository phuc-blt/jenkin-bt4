from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/check_prime/{num}")
def check_prime(num: int):
    if num < 2:
        return {"num": num, "is_prime": False}
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return {"num": num, "is_prime": False}
    return {"num": num, "is_prime": True}

@app.get("/get_version")
def get_version():
    return {"version": "1.0.0"}
