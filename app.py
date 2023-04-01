from flask import Flask, render_template, session, redirect, request
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
client=pymongo.MongoClient("mongodb+srv://mdharshaprada:MongoDB@cluster0.0hfnquj.mongodb.net/test")
db=client.get_database('primeBankofIndia')
collection = db["Responses"]
print(db)

def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# Routes
from user import routes

@app.route("/")    
def home():
    return render_template("index.html")  

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)