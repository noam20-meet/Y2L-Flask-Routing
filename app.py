from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route("/")
def home():
   return render_template("home.html" )
    
@app.route("/store")
def store():
	prodacts= quary_all()
   	return render_template("store.html" , Prodacts= prodacts)

@app.route('/add_prodact/<name>/<price>/<picturelink>/<description>')
def add_the_prodact(name, price, picturelink, description):
	add_prodact(name, price, picturelink, description)
	return render_template("store.html")

@app.route('/update_prodact/<name>/<price>/<picturelink>/<description>')
def uptade_the_prodact(name, price, picturelink, description):
	update_prodact(name, price, picturelink, description)
	return render_template("store.html")

@app.route('/delete_prodact/<their_price>')
def delete_the_prodact(their_price):
	delete_prodact(their_price)
	return render_template("store.html")

@app.route('/quary_all')
def quary_all_prodacts():
	add_to_cart()
	return render_template("cart.html")

@app.route('/quary_by_name/<their_name>')
def quary_by_name_prodacts():
	quary_by_name()
	return render_template("cart.html")

@app.route('/add_to_cart/<prodact_id>')
def add_cart():
	prodact_id=int(prodact_id)
	add_to_cart()
	return render_template("cart.html")
    
    

if __name__ == '__main__':
    app.run(debug=True)