from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, picturelink, description):
   
    product_object = Product(
    name= name,
    price= price,
    picturelink= picturelink,
    description= description)
    session.add(product_object)
    session.commit()



def update_product_status(name, price, picturelink,  description):
  
   product_object = session.query(
       Product).filter_by(
       name=name).first()
   product_object.price = price
   session.commit()


def delete_product(their_price):
  
   session.query(Product).filter_by(
      price=price ).delete()
   session.commit()




def query_all():
   
   products = session.query(
      Product).all()
   return products




def query_by_name(their_name):

   product = session.query(
       Product).filter_by(
       name=name).first()
   return product





def add_to_cart(product_id):

	cart_object = Cart(
	product_id=product_id)
	session.add(cart_object)
	session.commit()


add_product("noam", 10000, "selfie", "extra smart")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})








