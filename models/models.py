from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


Base = declarative_base()


class Company(Base):

    __tablename__ = "company"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    company_name = Column(String(255), nullable=False)
    address = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Company {self.company_name}>"


class Contact(Base):

    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    company_id = Column(Integer, ForeignKey("company.id"))
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    active = Column(Boolean, default=True, nullable=False)
    address = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    company = relationship("Company")
