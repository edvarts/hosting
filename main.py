from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
   return render_template('gugl.html')
@app.route("/learn")
def learn():
    return "<h1>es esmu kruts zens</h1> " \
           "<h2>tapec macos progot</h2>"

if __name__ == '__main__':
    app.run()