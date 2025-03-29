from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import search
import os
from dotenv import load_dotenv

#load env variables
load_dotenv()

#load origins allowed to request to api
origins = os.getenv("ALLOWED_ORIGINS")
origins = origins.split(",")

app = FastAPI()

#define app settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

#root route
@app.get("/")
def home():
    print(origins)
    return "Server running"

#include routes from search file
app.include_router(search.router)