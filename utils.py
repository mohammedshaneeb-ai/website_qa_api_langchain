from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer

from dotenv import load_dotenv
import os
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

chain = load_qa_chain(llm, chain_type="stuff",verbose=True)

def create_db(website_link):
    ## Load data

    file_path = "output.txt"


    loader = WebBaseLoader(website_link)
    data = loader.load()


    

    ## Splitting to chunks 
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=20)
    docs = splitter.split_documents(data)
    print(docs)

    ## Embedding
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    ## Vector Store
    db = Chroma.from_documents(docs,embedding)

    return db


def find_answer(query,db):
    template = """This is a website content. Use the following pieces of context to answer the question at the end. 
    only answer from this context if answer is not in the context say I don't know.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Use five sentences maximum and keep the answer as concise as possible,. 
    Always say "thanks for asking!" at the end of the answer. 
    {context}
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=db.as_retriever(),
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    )


    result = qa_chain({"query": query})
    return result["result"]


