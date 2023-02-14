from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.config.database import get_db, create_db, drop_db
from src.routes import user, lottery

app = FastAPI()
app.include_router(user.route)
app.include_router(lottery.route)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

