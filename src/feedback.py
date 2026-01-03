class ExplainableInterviewFeedback:
    def generate_feedback(self, expected_answer: str, user_answer: str):
        expected_words = set(expected_answer.lower().split())
        user_words = set(user_answer.lower().split())

        matched = expected_words & user_words
        missing = expected_words - user_words

        score = min(10, int((len(matched) / max(1, len(expected_words))) * 10))

        feedback = (
            "Great answer!" if score >= 8 else
            "Decent answer, but you missed some key points." if score >= 5 else
            "Answer needs improvement. Try covering the core concepts."
        )

        return {
            "score": score,
            "feedback": feedback,
            "missing_keywords": list(missing)
        }
