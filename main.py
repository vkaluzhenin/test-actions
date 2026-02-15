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


@app.get("/date")
def get_date():
    """Возвращает текущую дату в формате ISO (YYYY-MM-DD)."""
    return {"date": datetime.now().strftime("%Y-%m-%d")}


@app.get("/date/formatted")
def get_date_formatted():
    """Возвращает текущую дату в читаемом формате (дд.мм.гггг)."""
    return {"date": datetime.now().strftime("%d.%m.%Y")}
