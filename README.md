# Q&A on Website

This project is designed to facilitate Question Answering on websites, allowing users to ask any questions related to the current webpage they are viewing. The system is capable of providing accurate and contextually relevant answers to these queries.

This chatbot system offers significant benefits for blog websites, as it empowers users to obtain answers without the need to read through the entire content. This enhances the user experience by providing quick and precise information, ultimately improving user engagement and satisfaction.


## Table of Contents
- [Problem](#problem)
- [Installation](#installation)
- [Stacks](#Stacks)
- [Contributing](#contributing)

## What problem this chatbot solving
This bot addresses a common problem faced by users when visiting websites, particularly blog sites. The problem it solves is:

__Information Overload and Time-Consuming Content Navigation:__ Users often encounter lengthy articles or web pages with substantial amounts of information. Reading through all the content to find specific answers or relevant information can be time-consuming and overwhelming. Many users prefer quicker and more efficient ways to access the information they need.

The bot solves this problem by providing a user-friendly and efficient means of obtaining specific answers and information from a webpage. Users can simply ask questions related to the content they are viewing, and the bot leverages NLP technology to provide precise, context-aware responses. This streamlines the information retrieval process, saves users time, and enhances their overall experience on the website.



## Installation
#### Clone the repository

First, clone the GitHub repository to your local machine. You can do this using the git command

```bash
git clone https://github.com/mohammedshaneeb-ai/website_qa_api_langchain.git website_qa
```
#### Navigate to the Project Directory:
```bash
cd website_qa
```

#### Create a Virtual Environment (Optional but Recommended):
It's a good practice to create a virtual environment to isolate your project dependencies. This step is optional but highly recommended to avoid conflicts with other Python packages on your system.


```bash
python -m venv venv
```
#### Activate the virtual environment:
 * On Windows:
```bash
venv\Scripts\activate

```
 * On macOS or Linux:
```bash
source venv/bin/activate

```

#### Install Dependencies
Use pip to install the project's dependencies listed in the requirements.txt file. Run this command from the project directory:

```python
pip install -r requirements.txt
```

#### Run the FastAPI Application
Once you've installed the dependencies, you can run the FastAPI application
```python
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

#### Access the FastAPI Application
After starting the FastAPI application, you can access it by opening a web browser and navigating to the appropriate URL. By default, it should be available at http://localhost:8000 if you followed the command above.

If you're running the application on a server or in a different environment, replace localhost and 8000 with the appropriate hostname and port.

That's it! You should now have the FastAPI project up and running locally with all its dependencies installed


## Stacks Used

- GPT 3.5
- Langchain
- FAISS
- FastAPI   


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Acknowledgments

- I would like to extend  my gratitude to Langchain for providing a open source framework, which has significantly contributed to the success of this project


## Future Plans

Here are some of the planned features and improvements for this project in the near future. Your feedback and contributions are welcome and can help shape the direction of this project.

- **Summarization**: user will get Summarization of the whole page.
- **Conversational**: make this chatbot to Conversational.

## API Reference

#### Initial setup

```http
  POST /api/process_data
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `webpage_id` | `string` | **Required**. Your webpage id |
| `webpage_link` | `string` | **Required**. Your webpage link |

#### Get answer

```http
  GET /api/answer_quesion
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `webpage_id`      | `string` | **Required**. Id of webpage that given in process_data |
| `question` | `string` | **Required**. Your question|


