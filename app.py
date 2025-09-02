import streamlit as st
import os
from dotenv import load_dotenv
import requests
from huggingface_hub import InferenceClient
import json

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Code Roaster 🔥",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 2rem;
    }
    .roast-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #ff4b4b;
        margin: 1rem 0;
    }
    .success-container {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    .stSelectbox > div > div > select {
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

def get_system_prompt(roast_style):
    """Generate system prompt based on roast style"""
    prompts = {
        "😈 Savage": """You are a savage code reviewer with no mercy. Your job is to brutally roast the submitted code with sharp wit and brutal honesty. Point out every flaw, inefficiency, and questionable decisions. Use programming humor and be mercilessly funny. End with a brutal but hilarious summary.""",
        
        "🤡 Meme": """You are a meme-loving, internet-culture-savvy code reviewer. Roast the code using popular memes, internet references, and funny observations. Make jokes about coding stereotypes and use meme language. Be funny but educational.""",
        
        "🧑‍🏫 Friendly": """You are a friendly but witty coding mentor. Roast the code in a constructive way - point out issues with humor and gentle teasing, but always end with encouragement and helpful suggestions for improvement."""
    }
    return prompts.get(roast_style, prompts["🧑‍🏫 Friendly"])

def get_user_prompt(code):
    """Generate user prompt with the code to be roasted"""
    return f"""Please roast this code thoroughly:

```
{code}
```

Be specific about issues you find and make it entertaining!"""

def roast_code_with_huggingface(code, style="🧑‍🏫 Friendly"):
    """
    Roast code using Hugging Face API
    """
    try:
        # Get API token from environment
        hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
        if not hf_token:
            return "❌ Error: Hugging Face API token not found. Please check your environment variables."
        
        # Initialize the client
        client = InferenceClient(token=hf_token)
        
        # Get system and user prompts
        system_prompt = get_system_prompt(style)
        user_prompt = get_user_prompt(code)
        
        # Create messages
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        # Generate roast using chat completion
        response = client.chat_completion(
            messages=messages,
            model="mistralai/Mistral-7B-Instruct-v0.2",
            max_tokens=500,
            temperature=0.8
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ Error roasting your code: {str(e)}"

def main():
    # Header
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("🔥 Code Roaster 🔥")
    st.markdown("**Get your code brutally (or gently) roasted by AI!**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Roast style selection
    roast_style = st.selectbox(
        "Choose your roast style:",
        ["🧑‍🏫 Friendly", "😈 Savage", "🤡 Meme"],
        help="Select how brutal you want the roasting to be"
    )
    
    # Code input
    st.markdown("### 📝 Paste your code below:")
    code_input = st.text_area(
        "Code to roast:",
        height=200,
        placeholder="Paste your code here... Don't worry, we won't judge... much. 😏",
        help="Paste any code you want to get roasted!"
    )
    
    # Roast button
    if st.button("🔥 ROAST MY CODE! 🔥", type="primary", use_container_width=True):
        if code_input.strip():
            with st.spinner("🤖 AI is preparing to roast your code..."): 
                roast = roast_code_with_huggingface(code_input, roast_style)
                
                # Display roast
                if roast.startswith("❌"):
                    st.error(roast)
                else:
                    st.markdown('<div class="roast-container">', unsafe_allow_html=True)
                    st.markdown("### 🔥 Your Code Roast:")
                    st.markdown(roast)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Fun stats
                    st.markdown('<div class="success-container">', unsafe_allow_html=True)
                    st.markdown("### 📊 Roast Stats:")
                    st.markdown(f"- **Lines of code analyzed:** {len(code_input.splitlines())}")
                    st.markdown(f"- **Characters roasted:** {len(code_input)}")
                    st.markdown(f"- **Roast style:** {roast_style}")
                    st.markdown(f"- **Burn level:** {'🔥' * min(5, len(code_input) // 100 + 1)}")
                    st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please paste some code to roast!")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "Made with ❤️ and a lot of ☕ | Remember: All roasts are in good fun! 😄",
        help="This tool is meant for entertainment and learning purposes."
    )

if __name__ == "__main__":
    main()
