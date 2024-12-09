import streamlit as st
import google.generativeai as ai

#API key
API_KEY = 'AIzaSyC87bZtPgydD50X7rAqQiQad4XKjn0dpRs'

#configure the api
ai.configure(api_key=API_KEY)

#create a new model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# while True:
#     message = input('You : ')
#     if message.lower() == 'bye':
#         print('Chatbot : Goodbye!')
#         break
#     response = chat.send_message(message)
#     print('chatbot : ',response.text)
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Streamlit UI title
st.title("Chat with AI")

# Display the entire conversation history first
for message in st.session_state.chat_history:
    st.write(message)

# User input (Text box for chat input)
user_message = st.text_input("You: ", "")

# If the user has typed a message, send it to the chatbot
if user_message:
    # Send the message to the chatbot and get the response
    response = chat.send_message(user_message)
    
    # Append user message and chatbot response to chat history
    st.session_state.chat_history.append(f"You: {user_message}")
    st.session_state.chat_history.append(f"Chatbot: {response.text}")
    
    # Re-display the entire conversation history with the new messages
    for message in st.session_state.chat_history:
        st.write(message)

# If the user types 'bye', display a goodbye message
if user_message.lower() == 'bye':
    st.write("Chatbot: Goodbye!")