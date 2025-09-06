from fastapi import FastAPI
from app.routers import cricketer_route
app=FastAPI()

app.include_router(cricketer_route.routes)
