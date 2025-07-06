# 🧠📸 Gemini Pro - LLM & Image Model App

A powerful Python application that integrates Google's Gemini Pro model to handle both **textual prompts** and **image-based queries** using a seamless user interface. Built for AI/ML enthusiasts looking to explore multi-modal capabilities of large language models.

---

## 🚀 Features

- ✨ Ask questions using **text input**
- 🖼️ Analyze and respond to **image-based queries**
- 🤖 Powered by **Gemini Pro (via Google Generative AI)**
- 🧪 Streamlit-based interface for ease of use
- 📦 Clean and modular code structure

---

## 🛠️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/LLM_Image_Model_App_using_GeminiPro.git
cd LLM_Image_Model_App_using_GeminiPro
```

2. **Create a Virtual Environment (Optional but Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

1. Create a `.env` file in the root directory.
2. Add your **Google Generative AI API Key**:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## 🧪 Usage

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your browser.

---

## 📂 Project Structure

```
LLM_Image_Model_App_using_GeminiPro/
├── app.py              # Streamlit frontend app
├── vision.py           # Image query handling logic
├── requirements.txt    # Python dependencies
└── .env                # API Key (not tracked in Git)
```

---

## 🌟 Example Use Cases

- 📖 Ask questions like "Explain quantum mechanics in simple terms"
- 📷 Upload an image and ask "What disease does this leaf have?"

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repo and submit a pull request.

---

## 🙌 Acknowledgements

- [Google Generative AI](https://ai.google.dev)
- [Streamlit](https://streamlit.io)