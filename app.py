import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load NVIDIA API key from environment variable
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
NVIDIA_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL_NAME = "nvidia/llama3-chatqa-1.5-70b"

@app.route('/ask', methods=['POST'])
def ask_question():
    if not NVIDIA_API_KEY:
        return jsonify({"error": "NVIDIA API key not set in environment"}), 500

    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({"error": "Missing 'question' in request body"}), 400

    question = data['question']

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(NVIDIA_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        answer = result.get("choices", [{}])[0].get("message", {}).get("content", "")
        return jsonify({"answer": answer})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
