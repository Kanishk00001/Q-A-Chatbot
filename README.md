# Q-A Chatbot Collection

A comprehensive collection of different Question & Answer chatbot implementations using various AI technologies and approaches. This repository showcases multiple chatbot architectures from traditional Q&A systems to modern RAG-based implementations.

## Repository Structure

### 🤖 Chatbot Implementations

- **`OpenAi_Chatbot/`** - ChatGPT/OpenAI API-based chatbot implementation
- **`Ollama_Chatbot/`** - Local LLM chatbot using Ollama framework
- **`rag_qa_chatbot/`** - Retrieval-Augmented Generation Q&A system
- **`rag_document_chatbot/`** - Document-based RAG chatbot for file queries
- **`.devcontainer/`** - Development container configuration

## Features

- 🔥 **Multiple AI Approaches**: OpenAI API, Local LLMs, and RAG systems
- 📚 **Document Processing**: RAG-based chatbots for document querying
- 🏠 **Local & Cloud**: Both local (Ollama) and cloud-based (OpenAI) solutions
- ⚡ **Production Ready**: Containerized development environment
- 🎯 **Specialized Use Cases**: Different bots for different scenarios

## Quick Start

### Prerequisites

- Python 3.8+
- API keys (OpenAI, if using cloud services)

### Installation

```bash
# Clone the repository
git clone https://github.com/Kanishk00001/Q-A-Chatbot.git
cd Q-A-Chatbot

# Choose your chatbot implementation:

# For OpenAI Chatbot
cd OpenAi_Chatbot
pip install -r requirements.txt

# For Ollama Chatbot  
cd Ollama_Chatbot
pip install -r requirements.txt

# For RAG implementations
cd rag_qa_chatbot  # or rag_document_chatbot
pip install -r requirements.txt
```

## Configuration

Each chatbot has its own configuration:

- **OpenAI**: Requires `OPENAI_API_KEY`
- **Ollama**: Requires local Ollama installation

## Technologies Used

- **Python** - Core programming language
- **OpenAI API** - GPT models integration
- **Ollama** - Local LLM deployment
- **LangChain** - LLM application framework
- **Vector Databases** - For RAG implementations
- **Transformers** - Hugging Face models

## Development

Use the provided devcontainer for consistent development environment:

```bash
# Open in VS Code with devcontainer extension
code .
# Select "Reopen in Container"
```

## Comparison

| Implementation | Use Case | Pros | Cons |
|---------------|----------|------|------|
| OpenAI | General Q&A | High quality, fast | Requires API costs |
| Ollama | Privacy-focused | Local, free | Requires good hardware |
| RAG Q&A | Knowledge-based | Accurate, sourced | Complex setup |
| RAG Document | Document queries | Context-aware | Processing overhead |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-chatbot`)
3. Commit your changes (`git commit -m 'Add new chatbot implementation'`)
4. Push to the branch (`git push origin feature/new-chatbot`)
5. Open a Pull Request

## Author

**Kanishk** - [Kanishk00001](https://github.com/Kanishk00001)

## Acknowledgments

- OpenAI for GPT API
- Ollama team for local LLM framework
- LangChain community for RAG implementations

---

⭐ **Choose the right chatbot for your use case!** Each implementation serves different needs from cloud-based general Q&A to privacy-focused local processing.
