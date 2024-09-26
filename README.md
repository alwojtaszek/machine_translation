**Translation Toolkit Overview**

**Introduction**
This repository contains a multilingual translation app built using Streamlit for 
the frontend and OpenAI's GPT-4 API for the backend. Users can input text, 
select source and target languages, and receive translations. 
The app is containerized with Docker for easy local setup and scalable cloud deployment.

**Getting Started**
>1) Initial Setup: Clone the repository to your local machine. Ensure Python 3.x is installed on your system.
>2) Dependency Installation: Execute pip install -r requirements.txt in your terminal to install required libraries.
>3) Add your OPENAI_API_KEY to environment variables or set it in the code.
>4) Running the tool: streamlit run translator_app.py and follow the instructions there.

**Scalability Consideration**

To scale and deploy the translation app using cloud resources, I prepared the Docker to containerize the app, 
The Docker image would be pushed to a cloud platform like AWS, GCP, or Azure, where it would be deployed using a service  
like Kubernetes or Amazon ECS. 

>docker build -t translation-app . 

Define env variable OPENAI_API_KEY
>docker run -p 8501:8501 -e OPENAI_API_KEY translation-app