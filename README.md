# LawGPT: Legal Question Answering using NVIDIA NIM

This project is a Flask-based Python API that hosts NVIDIA's LLM model `nvidia/llama3-chatqa-1.5-70b` via the NVIDIA NIM API. It allows users to ask law-based questions and receive intelligent responses powered by NVIDIA's AI infrastructure.

---

## Features

- Hosts a local Flask server with a `/ask` endpoint
- Sends legal questions to NVIDIA NIM's LLM API
- Returns structured answers in JSON format
- Easy to deploy and test locally or on cloud platforms

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/LawGPT.git
cd LawGPT
