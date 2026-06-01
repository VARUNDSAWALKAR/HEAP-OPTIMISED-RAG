import sys
import os
import numpy as np
from heap_ranker import heap_top_k

# ---------- READ TXT FILE ----------
def read_txt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


# ---------- CHUNKING ----------
def chunk_text(text, chunk_size=200):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks


# ---------- EMBEDDING ----------
def embed(text, dim=50):
    rng = np.random.RandomState(abs(hash(text)) % (2**32))
    return rng.randn(dim)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# ---------- RETRIEVAL ----------
def retrieve_top_k(question, chunks, k=5):
    q_vec = embed(question)
    retrieved = []

    for chunk in chunks:
        sim = cosine_similarity(q_vec, embed(chunk))
        retrieved.append({
            "text": chunk,
            "similarity": sim
        })

    ranked = heap_top_k(retrieved, question, k)
    return [item[1]["text"] for item in ranked]


# ---------- ANSWER GENERATION ----------
def summarize_context(context_chunks, question):
    combined = " ".join(context_chunks)
    sentences = combined.split(".")

    q = question.lower().replace("?", "").strip()

    # ---------- STEP 1: Extract term from "WHAT IS X" ----------
    term = q
    if q.startswith("what is"):
        term = q.replace("what is", "").strip()

    # ---------- STEP 2: Definition sentence detection ----------
    for s in sentences:
        s_lower = s.lower()
        if term in s_lower and (
            "refer to" in s_lower
            or "is defined as" in s_lower
            or "is a" in s_lower
        ):
            return s.strip() + "."

    # ---------- STEP 3: Keyword-based fallback ----------
    q_words = [w for w in term.split() if len(w) > 3]
    selected = []

    for s in sentences:
        for w in q_words:
            if w in s.lower():
                selected.append(s.strip())
                break
        if len(selected) == 2:
            break

    if selected:
        return ". ".join(selected) + "."

    # ---------- STEP 4: Controlled failure ----------
    return "Answer not found in the given documents."

# ---------- MAIN ----------
if __name__ == "__main__":

    print("Paste TXT file paths one by one. Type DONE when finished.\n")

    files = []
    while True:
        path = input("> ")
        if path.lower() == "done":
            break
        files.append(path)

    all_text = ""
    for f in files:
        print(f"Reading: {f}")
        all_text += read_txt(f) + " "

    print("\nTOTAL TEXT LENGTH:", len(all_text))

    chunks = chunk_text(all_text)
    print("TOTAL CHUNKS:", len(chunks))

    if not chunks:
        print("❌ No text found.")
        exit()

    question = input("\nEnter your question:\n> ")

    top_chunks = retrieve_top_k(question, chunks, k=5)

    print("\nTOP-K CONTEXT (Ranked, One by One):\n")
    for idx, c in enumerate(top_chunks, start=1):
        print(f"--- Chunk {idx} ---")
        print(c[:350])
        print()

    print("\nFINAL ANSWER:\n")
    answer = summarize_context(top_chunks, question)
    print(answer)
