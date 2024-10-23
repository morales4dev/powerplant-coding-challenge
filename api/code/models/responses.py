"""
    This class provide the abstraction of some data sructures using pydantic library.
"""


from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    current_time: str
