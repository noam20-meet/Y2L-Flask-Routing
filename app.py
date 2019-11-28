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

@app.route('/add_product/')
def add_the_product():
	name =request.form["name"]
	price = request.form["price"]
	picturelink= request.form["picturelink"]
	description= request.form["description"]
	add_product(name, price, picturelink, description)
	return render_template("store.html")

@app.route('/update_product/')
def uptade_the_product():
	name =request.form["name"]
	price = request.form["price"]
	picturelink= request.form["picturelink"]
	description= request.form["description"]
	add_product(name, price, picturelink, description)
	return render_template("store.html")
	

@app.route('/delete_product/')
def delete_the_product(their_price):
	their_price= request.form["their_price"]
	delete_product(their_price)
	return render_template("store.html")

@app.route('/quary_all')
def quary_all_products():
	add_to_cart()
	return render_template("cart.html")

@app.route('/quary_by_name/')
def quary_by_name_products():
	their_name=request.form["their_name"]
	quary_by_name()
	return render_template("cart.html")

@app.route('/add_to_cart/')
def add_cart():
	product_id= request.form["product_id"]
	product_id=int(product_id)
	add_to_cart()
	return render_template("cart.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	error= None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error=error)


	
	

if __name__ == '__main__':
	app.run(debug=True)