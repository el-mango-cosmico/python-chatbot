# 🤖 Python Chatbot

Welcome to **Python Chatbot**! A local chatbot designed for easy and private use without relying on external services like ChatGPT.

## 📜 Features

- 🌐 **Local-first**: Your data stays on your machine.
- 🧠 Powered by **LangChain** and **LlamaCpp** for dynamic conversations.
- 🛠️ Fully customizable and extendable.

---

## 🚀 Getting Started

Follow these steps to set up and start using the chatbot!

### 🛠️ Prerequisites

- 🐍 Python **3.12+**
- 🛠️ Poetry for dependency management: [Install Poetry](https://python-poetry.org/docs/#installation)

### 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/python-chatbot.git
   cd python-chatbot
   ```

2. **Set Up the Environment**
   Run the setup command to install all dependencies and activate the environment:
   ```bash
   make setup
   ```

3. **Activate the Virtual Environment (if needed)**
   If the environment isn't already active, you can manually activate it:
   ```bash
   make activate
   ```

---

## 🏃‍♂️ Running the Chatbot

Start the chatbot with:
```bash
poetry run chatbot
```

Type your questions and enjoy the interaction! Type `exit` to quit the session.

---

## 📦 Adding New Models

To add new models to your chatbot, use the `download-model` Makefile command. Here’s an example for downloading the `llama-2-7b-chat.Q4_K_M.gguf` model from the `TheBloke` repository:

1. Run the command:
   ```bash
   make download-model
   ```

2. When prompted:
   - Enter the Hugging Face repository: `TheBloke/Llama-2-7b-Chat-GGUF`
   - Enter the model filename: `llama-2-7b-chat.Q4_K_M.gguf`

3. The model will be downloaded and saved into the `models/` directory.

---

## 🛡️ Troubleshooting

- **Poetry Not Installed**: If you see an error about Poetry, ensure it's installed correctly. Visit the [Poetry Docs](https://python-poetry.org/docs/#installation).
- **Model File Missing**: Ensure the required model files are downloaded into the `models/` directory.

---

## 🧪 Testing

Run tests to verify functionality:
```bash
pytest test/
```

---

## 🤝 Contributing

We welcome contributions! Feel free to submit issues or pull requests to improve the project.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Enjoy using the chatbot! 🎉
