from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():

    message = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        user_message = request.form["message"]

        message = f"Thank you {name}! Your message has been received."

    return render_template("contact.html", message=message)

@app.route("/services")
def services():
    return render_template("services.html")

if __name__ == "__main__":
    app.run(debug=True)