from flask import Flask, render_template, request, jsonify, redirect, url_for
from responses import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    response = get_response(user_input)
    return jsonify({"response": response})

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    print(f"Message received from {name} ({email}): {message}")
    return render_template("contact.html", success=True)

if __name__ == "__main__":
    app.run(debug=True)
