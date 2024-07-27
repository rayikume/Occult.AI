from fastapi import APIRouter
from Common.Database.database import book_collection
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

router = APIRouter()
model = OllamaLLM(model="llama3")

@router.get("/greet")
def handle_greet(promptlit):

    template = """use this prompt: {prompt}, and only generate 10 words that are similar to to it. NOTHING ELSE.
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