from pydantic import BaseModel
from typing import List, Optional

from pydantic import BaseModel
from typing import List, Optional

class FanBase(BaseModel):
    nome_completo: str
    local: str
    jogo_favorito: str
    modalidades: List[str]
    acompanha_esports: bool
    acompanha_streamers: bool
    redes_sociais: Optional[List[str]]

class FanCreate(FanBase):
    pass

class Fan(FanBase):
    id: int

    class Config:
        orm_mode = True
