from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Fan(Base):
    __tablename__ = "fans"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer)
    cidade = Column(String)
    jogo_favorito = Column(String)
    nivel_engajamento = Column(String)
    redes_sociais = Column(JSON)  # lista de URLs ou @s
