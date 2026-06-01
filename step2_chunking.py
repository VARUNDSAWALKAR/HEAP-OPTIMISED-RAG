from docx import Document

# -------- Step 1: Read document --------
path = r"C:\Users\nidag\Documents\rag_project\sample.docx"
doc = Document(path)

full_text = ""
for p in doc.paragraphs:
    if p.text.strip():
        full_text += p.text + " "

print("FULL DOCUMENT TEXT:\n")
print(full_text)


# -------- Step 2: Chunking function -------
def chunk_text(text, chunk_size=30):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    return chunks


# -------- Step 3: Apply chunking --------
chunks = chunk_text(full_text)

print("\nCHUNKS:\n")
for i, c in enumerate(chunks):
    print(f"Chunk {i+1}: {c}")
