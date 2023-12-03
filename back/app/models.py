from sqlalchemy import Column, DateTime, Float, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RpnCalculations(Base):
    """SQLAlchemy model for the rpn_calculations table"""

    __tablename__ = "rpn_calculations"

    id = Column(Integer, primary_key=True)

    time_executed = Column(DateTime(timezone=True), default=func.now())
    expression = Column(String)
    result = Column(Float, nullable=True)
