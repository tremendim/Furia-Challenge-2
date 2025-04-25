from pydantic import BaseModel
from typing import List, Optional

class FanBase(BaseModel):
    nome: str
    idade: Optional[int] = None
    cidade: Optional[str] = None
    jogo_favorito: Optional[str] = None
    nivel_engajamento: Optional[str] = None
    redes_sociais: Optional[List[str]] = []

class FanCreate(FanBase):
    pass

class Fan(FanBase):
    id: int

    class Config:
        orm_mode = True
