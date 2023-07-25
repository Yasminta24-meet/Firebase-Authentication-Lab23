from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  'apiKey': "AIzaSyBAjg9obJ5ADBbsk1njzkceiTgj9yguoBE",
  'authDomain': "yasminmeet1-96741.firebaseapp.com",
  'databaseURL': "https://yasminmeet1-96741-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "yasminmeet1-96741",
  'storageBucket': "yasminmeet1-96741.appspot.com",
  'messagingSenderId': "995722538562",
  'appId': "1:995722538562:web:00b30ae959cf8e859d47db",
  'measurementId': "G-EH46RK4LDP"
}

firebase= pyrebase.initialize_app(config)
auth= firebase.auth()
db = firebase.database()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error=''
    if request.method == 'POST':
        email= request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = 'Authentication failed'
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error=''
    if request.method == 'POST':
        # email= request.form['email']
        # bio = request.form['bio']
        # username= request.form['usernamee']
        # fullname= request.form['full_name']
        # password = request.form['password']
        # user = {'email':email, 'bio':bio, 'usernamee':username, 'full_name':fullname}
        try:
            email= request.form['email']
            print('d')
            bio = request.form['bio']
            print('d')
            username= request.form['usernamee']
            print('d')
            fullname= request.form['full_name']
            print('d')
            password = request.form['password']
            print('d')
            user = {'email':email, 'bio':bio, 'usernamee':username, 'full_name':fullname}
            print('d')
            print('d')
            
            print('d')
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            db.child('User').child(UID).set(user)
            print('d')
            return redirect(url_for('/'))
        except Exception as e:
            print(e)
            error = 'Authentication failed'
    return render_template("signup.html")

@app.route('/signout')
def signout():
    login_session['user']= None
    auth.current_user= None
    return redirect(url_for("signin"))

@app.route('/hi')
def hi():
    return redirect(url_for('add_tweet'))


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
        title1 = request.form['title']
        tweet1 = request.form['tweet']
        UID = login_session['user']['localId']
        tweets = {'title':title1, 'tweet':tweet1, 'uid':UID}
        db.child('Tweets').push(tweets)
        return redirect(url_for("all_tweets"))
    return render_template("add_tweet.html")

@app.route('/all_tweets', methods=['GET', 'POST'])
def all_tweets():
    tweets1 = db.child('Tweets').get().val()
    return render_template('tweets.html', tweets1=tweets1)




if __name__ == '__main__':
    app.run(debug=True)