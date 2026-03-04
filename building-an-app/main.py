from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    name = data.get("name")
    message = f"Hello {name}, your form was submitted successfully!"
    return jsonify({"response": message})

if __name__ == "__main__":
    app.run(debug=True)
