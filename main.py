from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.infra.config.database import create_db, drop_db
from src.routes import user_route, lottery_route, login_route

app = FastAPI()
app.include_router(user_route.route, tags=["user"])
app.include_router(lottery_route.route, tags=["lottery"])
app.include_router(login_route.router, tags=["auth"])

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


@app.middleware("http")
async def req_middleware(request: Request, next_call):
    print(f"Request: {request.headers}")
    response = await next_call(request)
    print(f"Response: {response}")
    return response
