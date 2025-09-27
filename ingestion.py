from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEmbeddings
#from langchain_openai import OpenAIEmbeddings
#from langchain_ollama import OllamaEmbeddings
#from langchain.embeddings import SentenceTransformerEmbeddings
#from langchain_community.embeddings import SentenceTransformerEmbeddings
#embedding = OllamaEmbeddings(
    #model="gemma3:270m"
#)
#embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

load_dotenv()
# giải thích quy trình lấy dữ liệu cho sufu nguyen nam nếu có tham khảo =)))
#Loader: lấy dữ liệu (WebLoader, PDFLoader, CSVLoader, …)

#ext Splitter: chia văn bản dài thành các chunk nhỏ (dễ tìm kiếm)

#Embeddings: dùng mô hình nhúng (OpenAI, Gemini, SentenceTransformers, Ollama embedding, …)

#Vector Store (ChromaDB, Pinecone, Weaviate, FAISS, …): lưu embeddings

#Retriever: khi user hỏi → tìm dữ liệu liên quan

#LLM: dùng kết quả tìm được để trả lời chính xác hơn (RAG).

urls = [
    # chưa tìm ra link tiếng nhật nên lấy tạm
"https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_list)

#vectorstore = Chroma.from_documents(
    #documents=doc_splits,
    #collection_name="rag-chroma",
    #embedding=embedding,
    #)

retriever = Chroma(
    collection_name="rag-chroma",
    persist_directory="./.chroma",
    embedding_function=embedding,
).as_retriever()