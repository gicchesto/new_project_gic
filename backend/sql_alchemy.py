import enum
from typing import List as List_, Optional as Optional_
from sqlalchemy import (
    create_engine, Column as Column_, ForeignKey as ForeignKey_, Table as Table_, 
    Text as Text_, Boolean as Boolean_, String as String_, Date as Date_, 
    Time as Time_, DateTime as DateTime_, Float as Float_, Integer as Integer_, Enum
)
from sqlalchemy.orm import (
    column_property, DeclarativeBase, Mapped as Mapped_, mapped_column, relationship
)
from datetime import datetime as dt_datetime, time as dt_time, date as dt_date

class Base(DeclarativeBase):
    pass



# Tables definition for many-to-many relationships

# Tables definition
class City(Base):
    __tablename__ = "city"
    id: Mapped_[int] = mapped_column(primary_key=True)
    Id: Mapped_[str] = mapped_column(String_(100))
    City: Mapped_[str] = mapped_column(String_(100))

class Person(Base):
    __tablename__ = "person"
    id: Mapped_[str] = mapped_column(String_(100), primary_key=True)
    Person: Mapped_[str] = mapped_column(String_(100))
    date_of: Mapped_[dt_date] = mapped_column(Date_)
    city_id: Mapped_[int] = mapped_column(ForeignKey_("city.id"))


#--- Relationships of the city table
City.person: Mapped_[List_["Person"]] = relationship("Person", back_populates="city", foreign_keys=[Person.city_id])

#--- Relationships of the person table
Person.city: Mapped_["City"] = relationship("City", back_populates="person", foreign_keys=[Person.city_id])

# Database connection
DATABASE_URL = "sqlite:///Class_Diagram.db"  # SQLite connection
engine = create_engine(DATABASE_URL, echo=True)

# Create tables in the database
Base.metadata.create_all(engine, checkfirst=True)