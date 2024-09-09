from fastapi import FASTAPI;

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Welcome to the Precision Agriculture Platform API"};
