from fastapi import APIRouter
router = APIRouter()

@router.post("/test-water")
def test_water(pH: float, conductivity: float, location: str):
    safe = 6.5 <= pH <= 8.5 and conductivity < 1000
    return {
        "location": location,
        "safe": safe,
        "advisory": "Safe" if safe else "Do not drink – use Tanker Y + aqua tabs"
    }