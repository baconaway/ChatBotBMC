import os
import openai
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import OpenAIChatbot

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app
api_key = ""
chatbot = OpenAIChatbot(api_key)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    assistant_message = chatbot.respond(user_message)
    return jsonify({"assistant_message": assistant_message})

if __name__ == '__main__':
    app.run(debug=True)
