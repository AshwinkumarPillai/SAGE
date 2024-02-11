from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import (
    MongoDBAtlasVectorSearch,
    DocArrayInMemorySearch,
)
from langchain_community.document_loaders import (
    PyPDFLoader,
    CSVLoader,
    TextLoader,
    WebBaseLoader,
)
from config import MONGODB_ATLAS_CLUSTER_URI, DB_NAME, COLLECTION_NAME
from langchain_community.vectorstores import MongoDBAtlasVectorSearch


def initialize_mongodb_client():
    from pymongo import MongoClient

    client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)
    return client[DB_NAME][COLLECTION_NAME]


def load_pdf_data(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()
    return split_documents(data)


def load_csv_data(file_path):
    loader = CSVLoader(file_path=file_path)
    return loader.load()


def load_text_data(file_path):
    loader = TextLoader(file_path)
    data = loader.load()
    return split_documents(data)


def load_data(file_path):
    if file_path.endswith(".pdf"):
        # Load data from PDF
        return load_pdf_data(file_path)
    elif file_path.endswith(".csv"):
        # Load data from CSV
        return load_csv_data(file_path)
    elif file_path.endswith(".txt"):
        # Load data from text file
        return load_text_data(file_path)
    else:
        raise "Unsupported file type"


def split_documents(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500, chunk_overlap=150
    )  # TODO: Need to Decide chunk size
    return text_splitter.split_documents(data)


def create_mongodb_atlas_vector_search(embedding, collection, index_name):
    return MongoDBAtlasVectorSearch(
        embedding=embedding,
        collection=collection,
        index_name=index_name,
    )


def perform_similarity_search(vector_search, query, k=5, pre_filter=None):
    return vector_search.similarity_search_with_score(
        query=query, k=k, pre_filter=pre_filter
    )


############################################################################################################
#  LOAD DATA DIRECTLY FORM URL
############################################################################################################
def load_url_data(urls: list[str]):
    loader = WebBaseLoader(urls)
    data = loader.load()
    return split_documents(data)


def create_in_memory_vector_search(docs, embedding):
    return DocArrayInMemorySearch.from_documents(docs, embedding)
