from fastapi import APIRouter
router = APIRouter()

@router.post("/report")
def create_report(ward: str, count: int):
    baseline = 3
    is_anomaly = count > baseline * 2
    return {
        "ward": ward,
        "count": count,
        "anomaly": is_anomaly,
        "message": f"Flagged because {count} vs {baseline} baseline" if is_anomaly else "Logged"
    }