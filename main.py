from fastapi import FastAPI
from pydantic import BaseModel
from utils import create_db,find_answer # Import your utility function


app = FastAPI()

class InputData(BaseModel):
    website_link: str
    user_id: str

user_vectorstores = {}


@app.post("/process_data/")
async def process_data(input_data: InputData):
    website_link = input_data.website_link
    user_id = input_data.user_id

    # Create a vectorstore instance based on the website_link (you need to implement this)
    db = create_db(website_link)

    # Store the vectorstore instance in the user_vectorstores dictionary
    user_vectorstores[user_id] = db

    return {"message": "Vectorstore assigned to user."}


@app.post("/answer_question/")
async def answer_question(question: str, user_id: str):
    # Retrieve the user's vectorstore instance from the dictionary
    db = user_vectorstores.get(user_id)

    if db is None:
        return {"error": "User not found or vectorstore not assigned."}

    # Use your utility functions to find the answer based on the question and the user's vectorstore instance
    answer = find_answer(question, db)  # Implement this function

    return {"answer": answer}

