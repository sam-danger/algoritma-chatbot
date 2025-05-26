
from flask import Flask, request, jsonify
import chatbot

app = Flask(__name__)

@app.route("/")
def home():
    return "Algoritma Chatbot Hazır!"

@app.route("/chatbot", methods=["POST"])
def bot_cevap():
    veri = request.get_json()
    girdi = veri.get("mesaj", "")
    cevap = chatbot.cevapla(girdi)
    return jsonify({"cevap": cevap})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
