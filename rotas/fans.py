from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from collections import Counter
import models
from database import get_db
import models, schemas

router = APIRouter(prefix="/fans", tags=["Fans"])

@router.post("/", response_model=schemas.Fan)
def create_fan(fan: schemas.FanCreate, db: Session = Depends(get_db)):
    db_fan = models.Fan(**fan.dict())
    db.add(db_fan)
    db.commit()
    db.refresh(db_fan)
    return db_fan

@router.get("/", response_model=List[schemas.Fan])
def read_fans(db: Session = Depends(get_db)):
    return db.query(models.Fan).all()


@router.get("/stats")
def get_estastiticas_fa(db: Session = Depends(get_db)):
    fans = db.query(models.Fan).all()

    total_fans = len(fans)
    if total_fans == 0:
        return {
            "message": "Nenhum fã cadastrado ainda."
        }

    jogos = Counter()
    redes = Counter()
    modalidades = Counter()
    esports_count = 0
    streamers_count = 0

    for fan in fans:
        jogos[fan.jogo_favorito] += 1
        if fan.redes_sociais:
            redes.update(fan.redes_sociais)
        modalidades.update(fan.modalidades)
        if fan.acompanha_esports:
            esports_count += 1
        if fan.acompanha_streamers:
            streamers_count += 1

    return {
        "top_jogos_favoritos": jogos.most_common(3),
        "redes_sociais_mais_usadas": redes.most_common(5),
        "modalidades_mais_acompanhadas": modalidades.most_common(5),
        "porcentagem_acompanha_esports": round((esports_count / total_fans) * 100, 2),
        "porcentagem_acompanha_streamers": round((streamers_count / total_fans) * 100, 2),
        "total_fas": total_fans
    }