from docx import Document
import numpy as np
import heapq
from transformers import pipeline

# ---------------- STEP 1: Read document ----------------
path = r"C:\Users\nidag\Downloads\SBT1401.pdf"
doc = Document(path)

full_text = ""
for p in doc.paragraphs:
    if p.text.strip():
        full_text += p.text + " "

# ---------------- STEP 2: Chunking ----------------
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

# ---------------- STEP 3: Embedding + Similarity ----------------
def embed(text, dim=50):
    rng = np.random.RandomState(abs(hash(text)) % (2**32))
    return rng.randn(dim)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# ---------------- STEP 4: Heap Top-K Retrieval ----------------
def retrieve_top_k(query, chunks, k=2):
    q_vec = embed(query)
    heap = []

    for i, chunk in enumerate(chunks):
        score = cosine_similarity(q_vec, embed(chunk))

        if len(heap) < k:
            heapq.heappush(heap, (score, i))
        else:
            if score > heap[0][0]:
                heapq.heapreplace(heap, (score, i))

    return [chunks[i] for _, i in sorted(heap, reverse=True)]

# ---------------- STEP 5: FINAL ANSWER GENERATION ----------------
print("\nLOADING LANGUAGE MODEL (first time may take 1–2 minutes)...\n")
generator = pipeline("text-generation", model="distilgpt2")

question = "What is RAG?"
top_chunks = retrieve_top_k(question, chunks, k=2)

context = " ".join(top_chunks)

prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

result = generator(prompt, max_length=150, num_return_sequences=1)

print("\nTOP-K CONTEXT:\n")
print(context)

print("\nFINAL ANSWER:\n")
print(result[0]["generated_text"])
