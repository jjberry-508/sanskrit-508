from flask import Flask, request, jsonify
from app.services import Services

app = Flask(__name__)
services = Services()


@app.route('/')
def hello() -> str:
    return "Welcome to the Sanskrit bot page"


@app.route("/generate", methods=["GET"])
def generate_words():
    services.generate_words()
    return jsonify({"msg": "success"})


@app.route("/parse", methods=["POST"])
def parse_word():
    data = request.get_json()
    forms = services.parse_word(data.get('word'))
    return jsonify(forms)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
