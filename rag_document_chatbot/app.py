import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama 
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with OLLAMA"

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's queries."),
    ("user", "Question: {question}")
])

# Generate response
def generate_response(question, engine, temperature, max_tokens):
    llm = Ollama(model=engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain.invoke({'question': question})

# Streamlit UI
st.title("🤖 Enhanced Q&A Chatbot with OLLAMA")

st.sidebar.title("🔧 Settings")
engine = st.sidebar.selectbox("Select a Model", ["gemma2:2b"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 50, 300, 150)

st.write("### 🗣️ Ask any question below:")
user_input = st.text_input("You:")

if user_input:
    try:
        response = generate_response(user_input, engine, temperature, max_tokens)
        st.write("**Assistant:**", response)
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
else:
    st.info("💡 Please enter a question to get started.")
