from fastapi import FastAPI
from app.database.database import connect_to_mongo, close_mongo_connection
from app.routers.router import router as form_router

app = FastAPI()

app.include_router(form_router)

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()


