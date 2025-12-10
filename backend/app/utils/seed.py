import pandas as pd
from app.models.kpi_model import KPIModel
from app.utils.database import SessionLocal
import os

def seed_data():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "kpis.csv")
    print(f"Loading CSV: {csv_path}")
    df = pd.read_csv(csv_path)

    db = SessionLocal()
    for _, row in df.iterrows():
        kpi = KPIModel(
            date=row["date"],
            revenue=row["revenue"],
            users=row["users"],
            conversion_rate=row["conversion_rate"],
            uptime=row["uptime"]
        )
        db.add(kpi)
    db.commit()
    db.close()

    print(f"Seeded {len(df)} KPI entries successfully.")

if __name__ == "__main__":
    seed_data()