from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(String, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    soil_moisture = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    