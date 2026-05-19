from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = ""

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        text = request.form.get("message")

        message = f"Děkujeme {name}, zpráva byla odeslána."

    return render_template("contact.html", message=message)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050)