from docx import Document
import numpy as np

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


# -------- Step 3: Embedding --------
def embed(text, dim=50):
    # Converts text into numbers (vector)
    rng = np.random.RandomState(abs(hash(text)) % (2**32))
    return rng.randn(dim)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# -------- Step 4: Compare with a question --------
question = "What is RAG?"
q_vec = embed(question)

print("\nSIMILARITY SCORES:\n")

for i, c in enumerate(chunks):
    c_vec = embed(c)
    score = cosine_similarity(q_vec, c_vec)
    print(f"Chunk {i+1} similarity: {score:.4f}")
