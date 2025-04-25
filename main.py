from fastapi import FastAPI
from database import Base, engine
import models
from rotas import fans

app = FastAPI(title="FURIA - Know Your Fan")

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# Inclui as rotas
app.include_router(fans.router)