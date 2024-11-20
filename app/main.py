from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from app.router import generate

app = FastAPI(
    title = "Template-Generator",
    version = "1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(generate.router)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs/")
    
    