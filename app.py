import streamlit as st
import requests

# Streamlit UI
st.title("🧠 LawGPT - Legal Question Answering")

api_key = st.text_input("🔑 Enter your NVIDIA API Key", type="password")
question = st.text_area("📜 Enter your legal question")

if st.button("Ask"):
    if not api_key:
        st.error("Please enter your NVIDIA API key.")
    elif not question.strip():
        st.error("Please enter a legal question.")
    else:
        payload = {
            "model": "nvidia/llama3-chatqa-1.5-70b",
            "messages": [{"role": "user", "content": question}]
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post("https://integrate.api.nvidia.com/v1/chat/completions", json=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
            answer = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            st.success("✅ Response:")
            st.write(answer)
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error: {str(e)}")
