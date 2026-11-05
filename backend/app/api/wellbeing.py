from fastapi import APIRouter
router = APIRouter()

@router.post("/check")
def check(household_id: str, phq2_score: int):
    return {
        "household_id": household_id,
        "mental_health_flag": phq2_score >= 3,
        "next_action": "Nudge PHC visit 9am"
    }