import heapq
import re

# ---------- KEYWORD OVERLAP ----------
def keyword_overlap_score(query, text):
    q_words = set(re.findall(r"\w+", query.lower()))
    t_words = set(re.findall(r"\w+", text.lower()))
    return len(q_words & t_words)


# ---------- HEAP-OPTIMIZED TOP-K ----------
def heap_top_k(chunks, query, k=5):
    """
    chunks: list of dicts
        {
            "text": str,
            "similarity": float
        }
    """

    heap = []
    q_clean = query.lower().replace("?", "")

    for chunk in chunks:
        text = chunk["text"]
        sim = chunk["similarity"]

        overlap = keyword_overlap_score(query, text)
        text_lower = text.lower()

        # 🔥 Definition boost (important for 'what is' questions)
        definition_boost = 0
        if q_clean in text_lower and "refer to" in text_lower:
            definition_boost = 5

        final_score = (0.6 * sim) + (0.3 * overlap) + definition_boost
        item = (final_score, chunk)

        if len(heap) < k:
            heapq.heappush(heap, item)
        else:
            if final_score > heap[0][0]:
                heapq.heapreplace(heap, item)

    return sorted(heap, key=lambda x: x[0], reverse=True)
