from sqlalchemy import Column, String, BIGINT
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base

class PeopleTable(Base):
    __tablename__ = "people"

    id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)

    pets = relationship("PetsTable", back_populates="owner")

    def __repr__(self):
        return (
            f"PEOPLE [name={self.first_name}, last_name={self.last_name}, age={self.age}, "
            f"pets={self.pets}]"
        )