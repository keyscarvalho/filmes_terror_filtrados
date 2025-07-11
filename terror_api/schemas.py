#%%

from pydantic import BaseModel
from typing import List

class Filme(BaseModel):
    titulo: str
    ano: int
    nota: float
    votos: int
    subgeneros: List[str]
    