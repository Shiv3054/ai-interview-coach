from fastapi import FastAPI
from pydantic import BaseModel
from src.feedback import ExplainableInterviewFeedback

app = FastAPI(title="AI Interview Coach API")

coach = ExplainableInterviewFeedback()

class EvaluateRequest(BaseModel):
    expected_answer: str
    user_answer: str

@app.post("/evaluate")
def evaluate(req: EvaluateRequest):
    return coach.generate_feedback(
        req.expected_answer,
        req.user_answer
    )
