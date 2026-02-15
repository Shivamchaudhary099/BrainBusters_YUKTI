import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/results')
def results():
    query = request.args.get('search')
    return render_template('results.html', query=query)


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    try:
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
   

