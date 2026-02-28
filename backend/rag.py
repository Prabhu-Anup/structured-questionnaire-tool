import re

def simple_keyword_match(question, documents):
    """
    Very basic keyword-based retrieval.
    """
    results = []

    question_words = set(re.findall(r"\w+", question.lower()))

    for doc in documents:
        doc_text = doc["text"].lower()
        match_score = sum(1 for word in question_words if word in doc_text)

        if match_score > 0:
            results.append({
                "text": doc["text"],
                "filename": doc["filename"],
                "score": match_score
            })

    # Sort by match score
    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:3]  # top 3 matches


def generate_answer_from_context(question, matched_docs):
    if not matched_docs:
        return "Not found in references.", None, "Low"

    top_doc = matched_docs[0]
    snippet = top_doc["text"][:300]
    score = top_doc["score"]

    # Confidence logic
    if score >= 5:
        confidence = "High"
    elif score >= 2:
        confidence = "Medium"
    else:
        confidence = "Low"

    answer = f"Based on internal documentation: {snippet}"

    return answer, top_doc["filename"], confidence