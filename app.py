from flask import Flask, render_template, request, jsonify
from agents.CookingAgent import generate_meals

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    data = request.get_json()

    ingredients = data.get("ingredients")

    if not ingredients:
        return jsonify({
            "response": "Please enter ingredients."
        })

    result = generate_meals(ingredients)

    return jsonify({
        "response": result
    })

if __name__ == "__main__":
    app.run(debug=True)