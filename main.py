from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/about-me", methods=["GET"])
def about():
    return render_template("about.html")
@app.route("/")
def index():
    personname = 'EDE'
    return render_template('index.html')
@app.route("/learn")
def learn():
    return "<h1>es esmu kruts zens</h1> " \
           "<h2>tapec macos progot</h2>"

if __name__ == '__main__':
    app.run()