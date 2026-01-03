from sentence_transformers import SentenceTransformer, util

class AnswerRelevanceEvaluator:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def score(self, expected_answer: str, candidate_answer: str) -> float:
        emb_expected = self.model.encode(expected_answer, convert_to_tensor=True)
        emb_candidate = self.model.encode(candidate_answer, convert_to_tensor=True)

        similarity = util.cos_sim(emb_expected, emb_candidate)
        return float(similarity[0][0])

