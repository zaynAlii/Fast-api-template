from fastapi import FastAPI 
from fastapi.responses import RedirectResponse
from contextlib import  asynccontextmanager


@asynccontextmanager
def lifespan(app:FastAPI):
    print("Starting Application")
    yield
    print("Shutting down")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def pushToDocs()->RedirectResponse:
    return RedirectResponse(url="/docs")

