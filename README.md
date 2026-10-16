# HEAP-OPTIMISED-RAG
Built an optimized Retrieval-Augmented Generation (RAG) system using SentenceTransformers and Chroma Vector Store for semantic search and high-quality response generation. Implemented a min-heap Top-K ranking module and composite scoring (semantic, keyword, domain weighting) to reduce retrieval latency and minimize hallucinations.


Heap-Optimized Retrieval-Augmented Generation (RAG) Pipelines to Enhance Contextual RelevanceA lightweight, efficient, and offline-capable Retrieval-Augmented Generation (RAG) system built entirely in Python using standard data structures like min-heaps (heapq) and vector similarity metrics to enhance contextual document retrieval and question answering.

📂 Repository Contents
This repository provides code and documentation for the experiential learning project developed under the Department of Computer Science and Engineering (Data Science) at RV College of Engineering, Bengaluru.   rag_logic.py: Core pipeline handling document ingestion, preprocessing, semantic chunking, pseudo-embedding generation, cosine similarity, and answer extraction.   heap_ranker.py: Priority-queue-based ranking mechanism utilizing min-heaps to optimize top-K document chunk retrieval. 


Project Report: Comprehensive documentation detailing architecture, methodologies, experimental evaluations, and appendices.

🚀 System Architecture & MethodologyTraditional full-sorting and exhaustive scan approaches in vector search introduce high computational overhead, scaling at $O(N \log N)$. This project replaces full sorting with a heap-based priority queue ranking mechanism, reducing the retrieval complexity to $O(N \log K)$.   Pipeline Flow:Document Ingestion & Preprocessing: Cleans and normalizes raw text documents to eliminate formatting noise.   Semantic Chunking: Splits documents into fixed-size semantic blocks (default chunk size: 200 words) while preserving context. 

Embedding Generation: Transforms text chunks and user queries into numerical vector representations.   Similarity Computation: Computes cosine similarity scores between the user query vector and document chunk vectors.  
Heap-Based Top-K Retrieval: Maintains a min-heap priority queue to dynamically retain only the top-$K$ highest scoring chunks based on a composite score combining cosine similarity, keyword overlap, and definition boosts.   Answer Generation: Extracts and summarizes concise, context-aware answers strictly grounded in the retrieved text. 

📊 Key Performance & Experimental FindingsAlgorithmic Efficiency: Replacing full-corpus sorting with a min-heap structure reduces retrieval overhead and scales efficiently as document volume grows.   Robustness: Evaluated against diverse query formats (factual, conceptual, and paraphrased queries), demonstrating high resilience against irrelevant queries without producing misleading outputs.   Privacy & Offline Usability: Operates entirely offline using standard local Python libraries (numpy, heapq), avoiding heavy cloud dependencies or external API costs.   

<img width="550" height="247" alt="image" src="https://github.com/user-attachments/assets/2aa11418-1db7-464e-b4ec-1d6b22dbd671" />
A heap-optimized, text-based Retrieval-Augmented Generation interface enabling efficient top-K document retrieval and accurate question answering.
<img width="563" height="212" alt="image" src="https://github.com/user-attachments/assets/dfef1b28-a9d4-4a72-b5da-4574f9a97d5e" />
The interface displays heap-ranked top-K relevant text chunks in response to a user query, ensuring transparent and context-aware information retrieval.



📊 Experimental Results & PerformanceEfficiency: The min-heap implementation bypasses expensive full-corpus sorting, lowering computational complexity from $O(N \log N)$ to $O(N \log K)$.  

Robustness: Evaluated against varied query formulations (factual, conceptual, and paraphrased queries), ensuring high retrieval accuracy without generating misleading information when context is absent.   Offline Capability: Fully functional locally in Python using standard libraries (numpy, heapq), avoiding heavy cloud APIs and protecting data privacy. 

👥 Authors & AffiliationInstitution: RV College of Engineering, Bengaluru - 560059, Karnataka, India 
Department: Department of Computer Science and Engineering (Data Science) 
Project Team:Shreesha S Koushik (1RV24CD048) 
Varun D Sawalkar (1RV24CD058)
Vikas Sidagouda Nidagunde (1RV24CD059)  
Guide: Prof. Mekhala Vinod Purohit   
