from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/realtimedb'
db = SQLAlchemy(app)

class Users(db.Model):
    user_id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    email = db.Column(db.String(40),unique=True)
    password = db.Column(db.String(40))
    
    def __init__(self,email,password):
        self.email = email
        self.password = password
#db.create_all()

@app.route('/',methods=['POST','GET'])
def index(): 
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            res = db.session.query(Users).filter(Users.email == email)
            for i in res:
                if(i.password == password):
                    return redirect('/dashboard')
                else:
                    return redirect('/')
        except:
            return redirect("/")
    return render_template('login.html')

@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        rePass = request.form['psw-repeat']
        if(password == rePass):
            user = Users(email,password)
            print(user)
            try: 
                db.session.add(user)
                db.session.commit()
                return redirect('/')
            except:
                return redirect('/signup')
        else:
            return redirect('/signup')
    return render_template('signup.html')

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/signtospeech")
def signtospeech():
    return render_template("signtospeech.html")

@app.route("/texttosign")
def texttosign():
    return "text to sign"

@app.route("/admindb")
def admindb():
    return "admin"

if __name__ == "__main__":
    app.run(debug=True)