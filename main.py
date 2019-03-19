from flask import Flask, render_template, request, make_response, g, redirect
from models import User
import random
import hashlib
import uuid

app = Flask(__name__)


# before_request nostrādā PIRMS KATRA PIEPRASĪJUMA
# pārbaudam vai lietotājs ir ielogojies
@app.before_request
def before_request():
    session_cookie = request.cookies.get("session")
    if session_cookie:
        g.active_session = session_cookie
        user = User.fetch_one(query=['session_token', '==', session_cookie])
        g.user_name = user.name


@app.route('/logout')
def logout():
    user = User.fetch_one(query=['session_token', '==', g.active_session])
    user.edit(user.id, session_token='-')  # reset session token
    response = make_response(redirect('/'))
    response.set_cookie('session', '', expires=0)  # izdzesam cookie
    return response


@app.route("/")
def index():
    personname = 'EDE'
    return render_template('index.html')
@app.route("/info.html", methods=['GET', 'POST'])
def info():
    return render_template('info.html')

@app.route("/bio.html")
def bio():
    return render_template('bio.html')
@app.route("/contact.html")
def contact():
    return render_template('contact.html')


@app.route('/connect.html', methods=['GET', 'POST'])
def connect():
    status = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = User.fetch_one(query1=["password", "==", hashed_password], query2=['email', '==', email])
        if user:  # successful login
            session_token = str(uuid.uuid4())
            user.edit(user.id, session_token=session_token)
            set_cookie = session_token
            response = make_response(redirect('/'))
            response.set_cookie('session', session_token)
            return response
        else:
            status = 'Nepareizs epasts vai parole!'
    return render_template('connect.html', status=status)

@app.route('/info.html', methods=['GET', 'POST'])
def atbilde():
    submit_text = request.form.get("message")
    if submit_text:
        user = User(atbilde=submit_text)
        user.create()

    answer_list = []
    user_list = User.fetch()
    for all_answers in user_list:
        answer_list.append(all_answers.answer)
    random_answers = random.sample(answer_list, 4)
    answer_1 = random_answers[0]
    answer_2 = random_answers[1]
    answer_3 = random_answers[2]
    answer_4 = random_answers[3]

    return render_template('info.html', answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4)



if __name__ == '__main__':
    app.run()



