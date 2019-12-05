from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *
from model import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route("/")
def home():
   return render_template("home.html" )
	
@app.route("/store")
def store():
	products= query_all()
	return render_template("store.html" , products= products)

@app.route("/about")
def about():
   return render_template("about.html" )

@app.route("/add_cart/1")
def add_cart(prodact_id):
	add_cart(prodact_id)
	return render_template("cart.html")

@app.route('/add_product')
def add_the_product():
	name =request.form["name"]
	price = request.form["price"]
	picturelink= request.form["picturelink"]
	description= request.form["description"]

	add_product(name, price, picturelink, description)
	return render_template("store.html")

@app.route('/update_product')
def uptade_the_product():
	name =request.form["name"]
	price = request.form["price"]
	picturelink= request.form["picturelink"]
	description= request.form["description"]
	uptade_the_product(name, price, picturelink, description)
	return render_template("store.html")
	

@app.route('/login', methods=['GET', 'POST'])
def login():
	error= None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
			return render_template("home.html")
		else:
			return render_template("portal.html" )
	else:
		return render_template('login.html', error=error)

	
@app.route('/portal' ,  methods=['GET', 'POST'])
def portal_edit():
	if request.method == 'GET':
		name =request.form["name"]
		price = request.form["price"]
		cc= request.form["picturelink"]
		description= request.form["description"]
		portal_edit(name, price, picturelink, description)
		uptade_the_product(name, price, picturelink, description)
		return render_template("store.html")
	

	
	

if __name__ == '__main__':
	app.run(debug=True)