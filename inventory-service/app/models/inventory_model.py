from sqlalchemy import Column
from sqlalchemy import Integer

from app.database.database import Base

class Inventory(Base):

    __tablename__ = "Inventory"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    product_id = Column(
        Integer,
        nullable=False
    )

    available_quantity = Column(
        Integer,
        nullable=False
    )