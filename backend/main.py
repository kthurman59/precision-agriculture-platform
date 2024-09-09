from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Welcome to the Precision Agriculture Platform API"};

@app.get("/readings")
def get_readings(db: Session = Depends(database.get_db)):
    readings = db.query(models.SensorReading).all()
    return readings
    