from fastapi import FastAPI
from app.routers import kpi
from app.utils.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(kpi.router)

@app.get("/ping")
def ping():
    return {"message": "pong"}