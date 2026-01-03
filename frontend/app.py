import streamlit as st
import difflib

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Interview Coach", layout="centered")

# ---------------- STYLES ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #fde2e4 0%, #e0f2fe 100%);
}

.block-container {
    padding-top: 3rem;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #1f2937;
}

.subtitle {
    text-align: center;
    color: #475569;
    margin-bottom: 30px;
}

.badge {
    display: inline-block;
    padding: 8px 22px;
    border-radius: 999px;
    background: linear-gradient(90deg, #ec4899, #6366f1);
    color: white;
    font-weight: 600;
    margin-bottom: 15px;
}

.card {
    background: rgba(255,255,255,0.9);
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 22px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
}

button {
    border-radius: 14px !important;
    background: linear-gradient(90deg, #ec4899, #6366f1) !important;
    color: white !important;
    font-weight: 600 !important;
}

.success {
    background: #dcfce7;
    padding: 16px;
    border-radius: 14px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="badge">AI-Powered Feedback Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="title">AI Interview Coach</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Explainable feedback for interview answers</div>', unsafe_allow_html=True)

# ---------------- INPUTS ----------------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    expected = st.text_area(
        "📌 Expected Answer",
        value="Machine learning is a subset of AI where models learn from data to make predictions without being explicitly programmed."
    )
    user = st.text_area(
        "🧠 Your Answer",
        value="Machine learning is part of AI where systems learn patterns from data and improve over time."
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- EVALUATION ----------------
def evaluate(expected, user):
    similarity = difflib.SequenceMatcher(None, expected.lower(), user.lower()).ratio()
    score = round(similarity * 10)

    strengths = []
    improvements = []

    if similarity > 0.6:
        strengths.append("Captures the core idea of machine learning.")
    if "data" in user.lower():
        strengths.append("Mentions learning from data.")

    if "prediction" not in user.lower():
        improvements.append("Mention prediction or output generation.")
    if len(user.split()) < 15:
        improvements.append("Answer is too short — expand explanation.")

    return score, strengths, improvements

# ---------------- BUTTON ----------------
if st.button("✨ Evaluate Answer"):
    score, strengths, improvements = evaluate(expected, user)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### ✅ Evaluation Complete")
    st.markdown(f"### 📊 Score: **{score} / 10**")

    st.markdown("### 💪 Strengths")
    if strengths:
        for s in strengths:
            st.markdown(f"- {s}")
    else:
        st.markdown("- Basic understanding demonstrated.")

    st.markdown("### 🔧 Improvements")
    if improvements:
        for i in improvements:
            st.markdown(f"- {i}")
    else:
        st.markdown("- Good answer overall. Add examples.")

    st.markdown('</div>', unsafe_allow_html=True)
