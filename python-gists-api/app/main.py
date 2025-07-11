from fastapi import FastAPI
from app.routers import gist_router

app = FastAPI()
app.include_router(gist_router.router)

@app.get("/")
def root():
    return {"message": "Visit /<username> like /octocat to get GitHub gists."}