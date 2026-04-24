from datetime import datetime, date, time
from typing import Any, List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator


############################################
# Enumerations are defined here
############################################

############################################
# Classes are defined here
############################################
class CityCreate(BaseModel):
    City: str
    person: Optional[List[int]] = None  # 1:N Relationship


class PersonCreate(BaseModel):
    date_of: date
    name: str
    city: int  # N:1 Relationship (mandatory)


