from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:Monday09@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://cfjnvpwotcyuyx:5e8b1d421d0a065389a3e38516c0b09aba066ada3a524c20a81fefca03eef1ce@ec2-54-78-142-10.eu-west-1.compute.amazonaws.com:5432/d4g7tr78vti02p'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route('/')
def index():
	result = Favquotes.query.all()
	return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
	 return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quotedata =Favquotes(author=author,quote=quote)
	db.session.add(quotedata)
	db.session.commit()

	return redirect(url_for('index'))




   	  #else:
		 #return render_template('quotes.html')
