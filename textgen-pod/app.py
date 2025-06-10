from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_API = "http://ollama:11434/api/generate"
DEFAULT_MODEL = "mistral"

@app.route("/", methods=["GET"])
def index():
    return '''
        <h2>Text-to-Text API ✅</h2>
        <form action="/analyze" method="post">
            <input type="text" name="text" placeholder="Enter your prompt"><br>
            <input type="text" name="model" placeholder="Model (optional, e.g., llama3)"><br>
            <button type="submit">Submit</button>
        </form>
    '''

@app.route("/analyze", methods=["POST"])
def analyze():
    user_input = request.form.get("text")
    model = request.form.get("model", DEFAULT_MODEL)

    if not user_input:
        return "<p style='color:red;'>No input text provided.</p>"

    payload = {
        "model": model,
        "prompt": user_input,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API, json=payload)
        response.raise_for_status()
        result = response.json().get("response", "").strip()
        return f"""
            <h2>Response from {model}:</h2>
            <pre>{result}</pre>
            <a href="/">🔙 Back</a>
        """
    except Exception as e:
        return f"<p style='color:red;'>❌ Error contacting Ollama: {str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5200)
