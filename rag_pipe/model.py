from langchain_google_genai import (
    ChatGoogleGenerativeAI,  # Chat Model
    GoogleGenerativeAIEmbeddings,
    GoogleGenerativeAI,  # Base LLM Model
)
from langchain_openai import (
    OpenAIEmbeddings,
    ChatOpenAI,  # Chat Model
    OpenAI,  # Base LLM Model
)

from config import GEMINI_API_KEY
from config import OPENAI_API_KEY


################################################################
#                       GOOGLE GENAI MODELs
################################################################
def initialize_gemini_chat_model():
    """
    The function initializes a chat model using the Gemini-Pro model from ChatGoogleGenerativeAI, with a
    specified Google API key and temperature.
    :return: The function `initialize_gemini_chat_model()` returns an instance of the
    `ChatGoogleGenerativeAI` class with the specified parameters.
    """
    return ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)


def initialize_gemini_base_llm_model():
    """
    The function initializes a GoogleGenerativeAI model with specific parameters.
    :return: an instance of the GoogleGenerativeAI class with the specified parameters.
    """
    return GoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)


################################################################
#                       OPENAI MODELs
################################################################
def initialize_openai_chat_model():
    return ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0.8)


def initialize_openai_base_llm_model():
    return OpenAI(api_key=OPENAI_API_KEY)


def initialize_openai_embedding_model():
    return OpenAIEmbeddings(api_key=OPENAI_API_KEY)
