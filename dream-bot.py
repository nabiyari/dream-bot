# app.py
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/', methods=['GET'])
def home():
    return "ربات تعبیر خواب فعال است"

@app.route('/interpret', methods=['POST'])
def interpret():
    data = request.get_json()
    user_sleep = data.get("dream")

    prompt = f"""
شما نقش یک کارشناس کامل و حرفه‌ای در زمینه تعبیر خواب دارید...
خواب: «{user_sleep}»
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "شما یک کارشناس حرفه‌ای تعبیر خواب هستید."},
            {"role": "user", "content": prompt}
        ]
    )

    return jsonify({"response": response.choices[0].message.content})
