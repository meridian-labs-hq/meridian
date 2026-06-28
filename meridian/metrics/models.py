from pydantic import BaseModel


class Metric(BaseModel):
    key: str
    name: str
    sql: str
    owner: str
    description: str = ""
