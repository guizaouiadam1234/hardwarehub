from fastapi import FastAPI

app = FastAPI()

#health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}