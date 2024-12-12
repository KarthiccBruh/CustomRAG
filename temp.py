from langchain.schema import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load or initialize the vector database
persist_directory = "./VectorDB/"

vectorstore = Chroma(
    persist_directory=persist_directory,
    _embedding_function=embedding_function,
)

query_embedding = vectorstore.embedding_function.embed_query("Vision Pro")
print("Query Embedding:", query_embedding)
