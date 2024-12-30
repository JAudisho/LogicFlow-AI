from flask import Flask, render_template, request, jsonify
from chatbot import get_chatbot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = get_chatbot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

print("Starting Flask app...")
app.run(debug=True)
print("Flask app terminated.")