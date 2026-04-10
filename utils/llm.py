from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini")

def ask_llm(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a code assistant.

    Answer the question based on the code context.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.predict(prompt)
    return response
