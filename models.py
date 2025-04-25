from sqlalchemy import Column, Integer, String, Boolean, JSON
from database import Base

class Fan(Base):
    __tablename__ = "fans"

    id = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String, nullable=False)
    local = Column(String, nullable=False)
    jogo_favorito = Column(String, nullable=False)
    modalidades = Column(JSON, nullable=False)  # Lista de modalidades (ex: ["CS:GO", "LoL"])
    acompanha_esports = Column(Boolean, default=False)
    acompanha_streamers = Column(Boolean, default=False)
    redes_sociais = Column(JSON, nullable=True)  # Ex: ["Instagram", "Twitter"]
