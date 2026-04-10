def get_relevant_chunks(vectorstore, query):
    docs = vectorstore.similarity_search(query, k=4)
    return docs
