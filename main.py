from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template("success.html")

@app.route("/about-me", methods=["GET"])
def about():
    return render_template("about.html")
@app.route("/")
def index():
    personname = 'EDE'
    return render_template('gugl.html')
@app.route("/learn")
def learn():
    return "<h1>es esmu kruts zens</h1> " \
           "<h2>tapec macos progot</h2>"

if __name__ == '__main__':
    app.run()