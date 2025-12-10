from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.kpi_model import KPIModel
from app.utils.database import SessionLocal

router = APIRouter(prefix="/kpis", tags=["KPIs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_all_kpis(db: Session = Depends(get_db)):
    return db.query(KPIModel).all()