from fastapi import FastAPI

app = FastAPI(title="Credit Risk Scoring API")

@app.get("/")
def health_check():
    return {"status": "ok"}
