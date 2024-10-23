"""
    This class provide the abstraction of the payload messages received from FUTURA API using pydantic library.



"""

from pydantic import BaseModel


class ProductionPlanItem(BaseModel):
    name: str
    p: float
