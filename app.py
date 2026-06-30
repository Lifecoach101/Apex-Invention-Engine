import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(page_title="Apex Invention Engine", page_icon="💡")

# Password protection logic
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False
    if st.session_state.password_correct:
        return True
    password = st.text_input("Enter Private Access Key", type="password")
    if password == "hrk2939Ppr13526!!#":
        st.session_state.password_correct = True
        st.rerun()
    elif password:
        st.error("Invalid Password")
    return False

# Main App Logic
def main():
    st.title("Apex Invention Engine")
    
    api_key = st.text_input("Enter Groq API Key", type="password")

    if api_key:
        client = Groq(api_key=api_key)

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "system", "content": "You are the 'Apex Invention Engine'. Your methodology is 'ROOTING': 1. ROOT ANALYSIS, 2. MINIMALIST EFFICIENCY, 3. MODULAR ADAPTATION, 4. DUALITY, 5. INNOVATION LOGIC. Always maintain this persona."}
            ]

        # Display chat history
        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        # Chat Input
        if prompt := st.chat_input("Describe your problem or invention idea..."):
            # Add user message to history
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    stream = client.chat.completions.create(
                        messages=st.session_state.messages,
                        model="llama-3.1-8b-instant",
                    )
                    response = stream.choices[0].message.content
                    st.markdown(response)
            
            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    if check_password():
        main()
