from fastapi import FastAPI
app = FastAPI(title="Sauti Tri-Sense API")

@app.get("/")
def root():
    return {"message": "Sauti Tri-Sense API – Population and Workforce Health Early Warning", "status": "MVP for Future Health Challenge 2026"}