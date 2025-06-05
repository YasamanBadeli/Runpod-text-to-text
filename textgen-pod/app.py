from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_API = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "mistral"  #Possible to change this to 'llama2', 'gemma'

@app.route("/analyze", methods=["POST"])
def analyze():
    user_input = request.form.get("text")
    model = request.form.get("model", DEFAULT_MODEL)

    if not user_input:
        return jsonify({"error": "No input text provided."}), 400

    payload = {
        "model": model,
        "prompt": user_input,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API, json=payload)
        response.raise_for_status()
        result = response.json().get("response", "").strip()
        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": f"Error contacting Ollama: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5200)
