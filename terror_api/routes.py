#%%

from fastapi import APIRouter, Query
from schemas import Filme
from database import df_filtrado
from typing import List



router = APIRouter()

@router.get("/filmes/", response_model=List[Filme])
def listar_filmes(nota_min: float = 0.0, votos_min: int = 0):
    resultado = df_filtrado[
        (df_filtrado["nota"] >= nota_min) &
        (df_filtrado["votos"] >= votos_min)
    ]
    return resultado.to_dict(orient="records")

@router.get("/filmes/subgenero/{subgenero}", response_model=List[Filme])
def filmes_por_subgenero(subgenero: str):
    resultado = df_filtrado[df_filtrado["subgeneros"].apply(lambda lista: subgenero.lower() in [s.lower() for s in lista])]
    return resultado.to_dict(orient="records")
