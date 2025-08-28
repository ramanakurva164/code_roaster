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
        "😈 Savage": """You are a savage code reviewer with no mercy. Your job is to brutally roast the submitted code with sharp wit and brutal honesty. Point out every flaw, inefficiency, and questionable decision. Be cutting but clever. Use humor, but make it sting. Don't hold back - this is a roasting session, not a code review.""",
        
        "🤡 Meme": """You are a meme-loving, internet-culture-savvy code reviewer. Roast the code using popular memes, internet references, and funny observations. Make jokes about coding stereotypes, use emojis, and reference popular programming memes. Keep it light-hearted but definitely make fun of the code. Think like a programmer who spends too much time on Reddit and Stack Overflow.""",
        
        "🧑‍🏫 Friendly": """You are a friendly but witty coding mentor. Roast the code in a constructive way - point out issues with humor and gentle teasing, but always end with encouragement and helpful suggestions. Think of yourself as that cool teacher who makes learning fun by poking fun at mistakes while still being supportive."""
    }
    return prompts.get(roast_style, prompts["🧑‍🏫 Friendly"])

def get_user_prompt(code):
    """Generate user prompt with the code to be roasted"""
    return f"""Please roast this code thoroughly:
