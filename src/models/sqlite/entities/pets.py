from sqlalchemy import Column, String, BIGINT, ForeignKey
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base

class PetsTable(Base):
    __tablename__ = "pets"

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    owner_id = Column(BIGINT, ForeignKey("people.id"), nullable=True)

    owner = relationship("PeopleTable", back_populates="pets")

    def __repr__(self):
        return f"Pets [name={self.name}, type={self.type}, owner_id={self.owner_id}]"