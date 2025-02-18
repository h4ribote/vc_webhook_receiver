from typing import Optional, Literal
from pydantic import BaseModel

class Currency(BaseModel):
    id:int
    name:str
    unit:str
    guild:int
    pool_amount:int


class PayerDiscord(BaseModel):
    id:int


class Payer(BaseModel):
    id:int
    discord:PayerDiscord


class ClaimUpdateEvent(BaseModel):
    id:int
    status:Literal['pending','approved','canceled','denied']
    amount:int
    updated_at:str
    metadata:dict
    payer:Payer
    currency:Currency


class WebhookPost(BaseModel):
    type:int
    data:Optional[list[ClaimUpdateEvent]] = None

