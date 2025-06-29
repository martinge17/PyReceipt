from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    name: str
    quantity: int
    price_per_unit: float


class Options(BaseModel):
    header_toggle: bool
    header: str | None = None
    footer_toggle: bool
    footer: str | None = None


class General(BaseModel):
    options: Options
    items: List[Item]
