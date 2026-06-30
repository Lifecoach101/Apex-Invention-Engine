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
    if password == "hrk2939Ppr13526!!#":  # <--- Yahan apna secret password paste kar dein
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
        try:
            client = Groq(api_key=api_key)
            challenge = st.text_area("Describe the problem you want to solve or the product you want to invent:")
            
            if st.button("Generate Invention"):
                if not challenge:
                    st.warning("Please describe your challenge first.")
                else:
                    # The ROOTING Methodology Prompt
                    system_prompt = """
                    You are the 'Apex Invention Engine'. Your methodology is 'ROOTING':
                    
                    1. ROOT ANALYSIS (The Asal): Deconstruct the problem to its absolute root. Ignore symptoms, focus on the cause.
                    2. MINIMALIST EFFICIENCY: Solve the problem using the least energy/resources. Prioritize micro-solutions over macro-complexities.
                    3. MODULAR ADAPTATION: Ensure the invention is scalable and adaptable for different environments (e.g., resource-poor vs. resource-rich).
                    4. DUALITY: Always consider how the invention can provide multi-functional utility (e.g., heating/cooling, financial/social).
                    5. INNOVATION LOGIC: Use First Principles to recombine existing technologies in unconventional, 'Asli' ways.

                    OUTPUT FORMAT:
                    ### ROOT ANALYSIS (The Asal)
                    [Breakdown of the core problem]
                    
                    ### MINIMALIST SOLUTION
                    [The leanest technical approach]
                    
                    ### MODULAR ARCHITECTURE
                    [How it adapts to different environments]
                    
                    ### IMPLEMENTATION (Step-by-Step)
                    [Actionable development roadmap]
                    """
                    
                    with st.spinner("Applying ROOTING methodology to your invention..."):
                        chat_completion = client.chat.completions.create(
                            messages=[
                                {"role": "system", "content": system_prompt}, 
                                {"role": "user", "content": challenge}
                            ],
                            model="llama-3.1-8b-instant", 
                        )
                        st.markdown(chat_completion.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    if check_password():
        main()
