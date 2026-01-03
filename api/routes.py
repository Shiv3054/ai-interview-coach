from fastapi import APIRouter
from pydantic import BaseModel
from src.feedback import ExplainableInterviewFeedback

router = APIRouter()
coach = ExplainableInterviewFeedback()

class EvaluateRequest(BaseModel):
    expected_answer: str
    user_answer: str

@router.post("/evaluate")
def evaluate(data: EvaluateRequest):
    result = coach.generate_feedback(
        data.expected_answer,
        data.user_answer
    )
    return result
