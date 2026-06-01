from docx import Document
import numpy as np
import heapq

# -------- Step 1: Read document --------
path = r"C:\Users\nidag\Documents\rag_project\sample.docx"
doc = Document(path)

full_text = ""
for p in doc.paragraphs:
    if p.text.strip():
        full_text += p.text + " "

# -------- Step 2: Chunking --------
def chunk_text(text, chunk_size=30):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

chunks = chunk_text(full_text)

print("CHUNKS:\n")
for i, c in enumerate(chunks):
    print(f"Chunk {i+1}: {c}")


# -------- Step 3: Embedding + Similarity --------
def embed(text, dim=50):
    rng = np.random.RandomState(abs(hash(text)) % (2**32))
    return rng.randn(dim)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# -------- Step 4: Heap‑based Top‑K Retrieval --------
def retrieve_top_k(query, chunks, k=2):
    q_vec = embed(query)
    heap = []   # min‑heap

    for i, chunk in enumerate(chunks):
        score = cosine_similarity(q_vec, embed(chunk))

        if len(heap) < k:
            heapq.heappush(heap, (score, i))
        else:
            if score > heap[0][0]:
                heapq.heapreplace(heap, (score, i))

    # Sort heap from best to worst
    top_chunks = [chunks[i] for score, i in sorted(heap, reverse=True)]
    return top_chunks


# -------- Step 5: Test --------
question = "What is RAG?"
top_chunks = retrieve_top_k(question, chunks, k=2)

print("\nTOP‑K CHUNKS:\n")
for t in top_chunks:
    print("-", t)
