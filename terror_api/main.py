#%%

from fastapi import FastAPI
from routes import router

app = FastAPI(title="API de Filmes de Terror")
app.include_router(router)

