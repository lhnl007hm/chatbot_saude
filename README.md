# 🌟 Premium Emotional Support Chatbot (Web)

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-2.3-green?logo=flask)](https://flask.palletsprojects.com/)  
[![Google Generative AI](https://img.shields.io/badge/Google_Generative_AI-Model-orange)](https://developers.generativeai.google/)  
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)  

A **web-based chatbot** that provides empathetic and positive support for emotional well-being. Built using **Python Flask** and the **Google Gemini 1.5 AI model**, this chatbot acts as a virtual friend, offering short, encouraging responses and helpful suggestions.

---

## 💡 Features

- ✅ Short, natural, and friendly responses  
- ✅ Personalized experience (remembers the user's name)  
- ✅ Persistent memory between sessions (`memoria_usuario.json`)  
- ✅ Automatic suggestions for relaxing activities  
- ✅ Periodic check-ins to encourage emotional well-being  
- ✅ Responsive web interface (Enter key or Send button)

---

## 🛠 Technologies

- Python 3.13  
- Flask – Web backend  
- Google Generative AI – Gemini 1.5 for generating responses  
- HTML / CSS / JavaScript – Interactive frontend  
- JSON – Persistent user memory

---

## 📁 Project Structure

```shell
$ tree
chat_web_natural/
├─ app.py # Flask backend
├─ memoria_usuario.json # Persistent user memory
├─ demo.gif # GIF demonstration of the chat
├─ templates/
│ └─ index.html # Frontend chat interface
├─ static/
└─ style.css # Chat styling
```

---

## 🚀 How to Run

1. Clone the repository and navigate into the folder:

```bash
git clone https://github.com/your-username/chatbot_saude.git
cd chatbot_saude
```

---

## (Optional) Create a virtual environment:

```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

---

## Install dependencies:

```bash
pip install flask google-generativeai
```

---

## Configure your Google Generative AI API key in app.py:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

---

## Run the Flask server:

```bash
python app.py
```

---

## Open your browser at:

```cpp
http://127.0.0.1:5000/
```

---

## 💬 Usage

- Type a message and press Enter or click Send
- The chatbot responds in a short, friendly, and encouraging manner
- Say “my name is [Your Name]” to personalize responses
- Conversations and user info are saved in memoria_usuario.json

---

## ⚡ Next Steps / Improvements

- 💌 Daily motivational messages automatically
- 🎨 Typing animation for the assistant to enhance realism
- 🔍 Detect stress-related keywords and suggest professional support
- 🌐 Multi-language support for broader accessibility
- 🖼 Add more GIFs or screenshots for visualization

---

## ⚠ Disclaimer

This chatbot does not replace professional mental health care.
It provides emotional support and positive suggestions. In case of emergencies, always contact a qualified professional immediately.

---
