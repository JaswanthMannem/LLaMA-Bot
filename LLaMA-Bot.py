from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st

# Define a prompt template for the chatbot
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the questions"),
        ("user","Question:{question}")
    ]
)

# Set up the Streamlit framework
st.title('LLaMA-Bot')  # Set the title of the Streamlit app

# Initialize the Ollama model
llm = Ollama(model="llama3")

# Create a chain that combines the prompt and the Ollama model
chain = prompt | llm

# Initialize session state to keep track of the conversation
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Text input for the user's question
user_input = st.text_input("Ask your question!", key='user_input')

# Button to submit the question
if st.button("Submit"):
    if user_input:
        response = chain.invoke({"question": user_input})
        st.session_state.conversation.append(("You", user_input))
        st.session_state.conversation.append(("Bot", response))

# Display the conversation history
st.write("### Conversation History")
for speaker, text in st.session_state.conversation:
    st.write(f"*{speaker}:* {text}")

# Text area to clear conversation history
if st.button("Clear Conversation"):
    st.session_state.conversation = []