from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()






#Fake Restaurants
#restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

#restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
#items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
#item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}

@app.route('/restaurant/JSON')
def restaurantsJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify([r.serialize for r in restaurants])
   # return jsonify(restaurants=[r.serialize for r in restaurants])





# This route will show all restaurants
@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)

# This route will make a new restaurant
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    return render_template('newrestaurant.html', restaurant=restaurant, items=items) 

# This route will edit a restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    return render_template('editrestaurant.html', restaurant_id=restaurant_id, items=items)  


# This route will delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    return render_template('deleterestaurant.html', restaurant_id=restaurant_id, items=items)

# This route will show menu for a restaurant
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    return render_template('menu.html', restaurant=restaurant, items=items)
 

@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
   # return "This page is for making a new menu item for restaurant %s" %restaurant_id  
   return render_template('newmenuitem.html', restaurant_id=restaurant_id, items_id=items_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:items_id>/edit/') 
def editMenuItem(restaurant_id, items_name):
   # return "This page is for editing menu item %s" %menu_id
    return render_template('editmenuitem.html', restaurant_id=restaurant_id, items_id=items_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:item_id>/delete/')
def deleteMenuItem(restaurant_id, item_id):
    #return "This page is for deleting menu item %s" %menu_id  
    return render_template('deletemenuitem.html', restaurants_id=restaurants_id, items_id=items_id)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
