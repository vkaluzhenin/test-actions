from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """Возвращает текущее время сервера."""
    return {"server_time": datetime.now().isoformat()}


@app.get("/time")
def get_time():
    """Альтернативный эндпоинт для получения текущего времени."""
    return {"server_time": datetime.now().isoformat()}
