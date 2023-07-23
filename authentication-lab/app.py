from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyBAjg9obJ5ADBbsk1njzkceiTgj9yguoBE",
  "authDomain": "yasminmeet1-96741.firebaseapp.com",
  "projectId": "yasminmeet1-96741",
  "torageBucket": "yasminmeet1-96741.appspot.com",
  "messagingSenderId": "995722538562",
  "appId": "1:995722538562:web:00b30ae959cf8e859d47db",
  "measurementId": "G-EH46RK4LDP"
};

firebase= pyerbase.initialize_app(config)
auth= firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error=''
    if request.method == 'POST':
        email= request.form['email']
        password = request.form['password']
        try:
            login_session['user']=
            auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = 'Authentication failed'
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error=''
    if request.method == 'POST':
        email= request.form['email']
        password = request.form['password']
        try:
            login_session['user']=
            auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = 'Authentication failed'
    return render_template("signup.html")

@app.route('/signout')
def signout():
    login_session['user']= None
    auth.current_user= None
    return redirect(url_for("signin"))


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)