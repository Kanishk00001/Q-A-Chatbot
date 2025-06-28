import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Langsmith tracking (optional)
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with OpenAI"

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's queries."),
    ("user", "Question: {question}")
])

# Generate response function
def generate_response(question, api_key, engine, temperature, max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model=engine, temperature=temperature, max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Streamlit UI
st.title("🤖 Enhanced Q&A Chatbot with OpenAI")

st.sidebar.title("🔧 Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
engine = st.sidebar.selectbox("Select an OpenAI Model", ["gpt-4o", "gpt-4-turbo", "gpt-4"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

st.write("### 🗣️ Ask any question below:")
user_input = st.text_input("You:")

if user_input:
    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar.")
    else:
        try:
            response = generate_response(user_input, api_key, engine, temperature, max_tokens)
            st.write("**Assistant:**", response)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
else:
    st.info("💡 Please enter a question to get started.")
