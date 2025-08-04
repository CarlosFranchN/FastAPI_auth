from fastapi import FastAPI
from app.db.sessions import engine
from app.models import user
from app.api.routes import auth_router
user.Base.metadata.create_all(bind=engine)

app = FastAPI()

user.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello" : "World"}

app.include_router(
    auth_router.router,
    prefix="/auth",
    tags=["Authentication"]               
                   )