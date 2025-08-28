# 🔥 Code Roaster

A fun Streamlit app that lets you paste code and get hilarious AI-generated roasts in different styles!

## 🚀 Features

- **Code Input**: Paste any programming language code
- **Multiple Roast Styles**:
  - 😈 **Savage**: Brutally honest, no mercy roasting
  - 🤡 **Meme**: Internet culture and meme-based humor
  - 🧑‍🏫 **Friendly**: Constructive criticism with humor
- **AI-Powered**: Uses Qwen/Qwen2.5-72B-Instruct via Hugging Face
- **Real-time Streaming**: Watch your roast appear in real-time
- **Fallback System**: Multiple API methods for reliability

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ramanakurva164/code-roaster.git
cd code-roaster
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Get your Hugging Face API token:
   - Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
   - Create a new token with "Read" permissions
   - Copy the token

3. Edit `.env` file and add your token:
   ```
   HF_TOKEN=your_actual_hugging_face_token_here
   ```

### 4. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🎯 How to Use

1. **Paste Your Code**: Copy and paste any code snippet into the text area
2. **Choose Roast Style**: Select your preferred roasting style from the dropdown
3. **Get Roasted**: Click "🔥 Roast Me! 🔥" and watch the AI roast your code
4. **Enjoy**: Laugh at the witty commentary about your code!

## 🏗️ Technical Details

### Architecture
- **Frontend**: Streamlit for the web interface
- **AI Backend**: Hugging Face Inference with Qwen/Qwen2.5-72B-Instruct
- **API Methods**: 
  - Primary: Chat Completions API (with streaming)
  - Fallback: Inference REST API

### File Structure
```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variable template
├── .env               # Your actual environment variables (not in git)
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## 🎨 Roast Styles Explained

### 😈 Savage
- No mercy, brutal honesty
- Sharp wit and cutting remarks
- Points out every flaw without sugar-coating

### 🤡 Meme
- Internet culture references
- Programming memes and jokes
- Light-hearted but definitely making fun

### 🧑‍🏫 Friendly
- Constructive criticism with humor
- Gentle teasing with helpful suggestions
- Educational but still entertaining

## 🚨 Troubleshooting

### Common Issues

1. **"Hugging Face token not found"**
   - Make sure you created the `.env` file
   - Check that your token is correctly set in the `.env` file
   - Ensure the token has the right permissions

2. **API Failures**
   - The app has a fallback system that tries multiple API methods
   - If both fail, it might be a temporary Hugging Face issue
   - Check your internet connection and token validity

3. **Slow Responses**
   - The Qwen-72B model is large and may take time to respond
   - Peak usage times might cause delays
   - The app shows loading indicators while waiting

### Getting Help

If you encounter issues:
1. Check that all dependencies are installed correctly
2. Verify your Hugging Face token is valid and has correct permissions
3. Try restarting the Streamlit app

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest new roast styles
- Improve the UI/UX
- Add new features

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Hugging Face](https://huggingface.co/)
- Uses [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) model

---

**Have fun roasting your code! 🔥**