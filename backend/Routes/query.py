from fastapi import APIRouter
from Common.Database.database import book_collection
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

router = APIRouter()
model = OllamaLLM(model="llama3")

@router.get("/greet")
def handle_greet(promptlit):

    template = """You are an AI assistant called Nerd AI that greet bookworms and ask if they want any book suggestions.
    always begin your reply with 'erm... Actually' and always have the tone of a nerdy guy that sees himself as highly intellectual person.
    bookworms input: {prompt}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        'prompt': promptlit,
    })

    # db = book_collection.query(
    #     query_texts=response,
    #     n_results=5
    # )

    return response