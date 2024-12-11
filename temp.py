from langchain_chroma import Chroma
from langchain_nomic.embeddings import NomicEmbeddings
import os

try:
    # Ensure the directory exists
    persist_directory = "C:/Users/karti/Desktop/mine"
    os.makedirs(persist_directory, exist_ok=True)

    # Try initialization with error handling
    try:
        vectorstore = Chroma(
            persist_directory=persist_directory, 
            embedding_function=NomicEmbeddings(
                model="nomic-embed-text-v1.5", 
                inference_mode="local"
            )
        )
        print("Vectorstore loaded successfully!")
    
    except Exception as init_error:
        print(f"Error initializing Chroma vectorstore: {init_error}")
        
        # Alternative embedding approach
        from sentence_transformers import SentenceTransformer
        
        class FallbackEmbeddings:
            def __init__(self):
                self.model = SentenceTransformer('all-MiniLM-L6-v2')
            
            def __call__(self, texts):
                return self.model.encode(texts).tolist()
        
        try:
            vectorstore = Chroma(
                persist_directory=persist_directory, 
                embedding_function=FallbackEmbeddings()
            )
            print("Fallback embedding method used successfully!")
        
        except Exception as fallback_error:
            print(f"Fallback method failed: {fallback_error}")

except Exception as dir_error:
    print(f"Directory creation error: {dir_error}")