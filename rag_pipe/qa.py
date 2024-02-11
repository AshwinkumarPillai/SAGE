from langchain.chains import RetrievalQA


def initialize_qa_retriever(vector_search):
    """
    The function `initialize_qa_retriever` initializes a question-answering retriever using a vector
    search model.
    
    :param vector_search: The parameter "vector_search" is an object that represents a vector search
    index. It is used to perform similarity searches on a collection of vectors
    :return: The function `initialize_qa_retriever` returns a retriever object that is initialized with
    a vector search. The retriever is configured to perform similarity search and retrieve the top 10
    most similar items.
    """
    return vector_search.as_retriever(search_type="similarity", search_kwargs={"k": 10})


def initialize_qa(llm, retriever, prompt_template):
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt_template},
    )
