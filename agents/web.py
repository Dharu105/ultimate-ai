from duckduckgo_search import DDGS

def ask_web(question):

    with DDGS() as ddgs:
        results = ddgs.text(question, max_results=5)

    context = "\n\n".join([r["body"] for r in results])

    return f"""
Web Answer:

{context}

Question: {question}
"""