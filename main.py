from fastapi import FastAPI
from pydantic import BaseModel
from utils import create_db,find_answer 


app = FastAPI()

class InputData(BaseModel):
    website_link: str
    webpage_id: str

website_vectorstores = {}


@app.post("/process_data/")
async def process_data(input_data: InputData):
    website_link = input_data.website_link
    webpage_id = input_data.webpage_id

    # Create a vectorstore instance based on the website_link 
    db = create_db(website_link)

    # Store the vectorstore instance in the website_vectorstores dictionary
    website_vectorstores[webpage_id] = db

    return {"message": "Vectorstore assigned to Webpage."}


@app.post("/answer_question/")
async def answer_question(question: str, webpage_id: str):
    # Retrieve the website's vectorstore instance from the dictionary
    db = website_vectorstores.get(webpage_id)

    if db is None:
        return {"error": "webpage not found or vectorstore not assigned."}

    # Using utility functions to find the answer based on the question and the website's vectorstore instance
    answer = find_answer(question, db)  

    return {"answer": answer}

