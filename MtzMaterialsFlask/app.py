# Flask imports for the web application, allows templates and url based commands to work
from flask import Flask, render_template, make_response, url_for, request, redirect
# Import Date & Time used for the connection to the Arduino (not implemented)
from datetime import datetime

# Class Model for the Databse
from Order import db, Orders
# allows http requests
import requests
# used to make json format
import json
# generates random number
import random

# Creates Flask application
app = Flask(__name__)

# Conection String used for mysql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/mtz-materials'

# Connection String used for a sqlitte database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

# allows database to be created
app.app_context().push()

# Error handling for pages not found, 404 Error
@app.errorhandler(404)
  
# inbuilt function which takes error as parameter
def not_found(e):
# 404 Error page 
  return render_template("404.html")

# Landing page used to display the weight from the scale
@app.route("/")
def index():
    # calls the 
    gross = data().json
    return render_template('index.html', gross = gross)

# Create Order Method, Returns Create Order page
@app.route("/createOrder")
def createOrder():
    return render_template('inputTare.html')

# Create Order method, GET method displays page, POST submits the form
@app.route("/createOrderForm", methods=['POST', 'GET'])
def createOrderForm():
        # If form is submitted, read all the properties
        if request.method == 'POST':
            truckId = request.form['truckId']
            truckCo = request.form['truckCo']
            customer = request.form['customer']
            job = request.form['job']
            product = request.form['product']
            gross = request.form['gross']
            tare = request.form['tare']
            net = request.form['net']
            tons = request.form['tons']
          
            try:
                # Use Properties to create new Order Object
                newOrder = Orders(truckId = truckId, truckCo = truckCo, customer = customer, job= job, product = product, gross = gross, tare = tare, net= net, tons = tons)
                # adds Order to databse
                db.session.add(newOrder)
                # commit to database
                db.session.commit()
                # return home page
                return render_template('index.html')
            #General exception handler
            except Exception as e:
                # print error
                print(e)
                return 'There was an issue creating your Order'

        else:
            # Get method used to read Tare from previous page, tare page
            inTare = request.args.get("inTare")

            # converts message into a float
            tare = float(inTare)
            
            # calculates the net using the gross weight from reading the scale
            net = data().json - tare         

            # generates tons 
            tons = net / 2000
            # returns page and parameters with it 
            return render_template('createOrder.html', gross = data().json, tare = tare, net = net, tons = ("{:.2f}".format(tons)))


# View one order Method, uses POST, and get redirects to view all orders
@app.route("/viewOneOrder/<int:orderId>", methods=['GET','POST'])
def viewOneOrder(orderId):
    # if order has been selected
    if request.method == 'POST':
        # gets the order by ID
        order = Orders.query.get(orderId)
        # returns update page and sends order
        return render_template('updateOrder.html', order = order)
    else:
        # redirects to view all orders
        return redirect('/viewOrders')

# View all orders
@app.route("/viewOrders")
def viewOrders():
    # selects all orders from database
    orderList = Orders.query.all()
    # returns view all order page and list of orders
    return render_template('viewOrders.html', orderList = orderList)

# Update Order Page
@app.route("/updateOrder", methods=["POST"])
def updateOrder():

    # Gets Order ID from previous page
    orderId = request.form['orderId']

    # selects order from database
    order = Orders.query.get(orderId)
    
    # Reads all changes from the update order page
    order.truckId = request.form['truckId']
    order.truckCo = request.form['truckCo']
    order.customer = request.form['customer']
    order.job = request.form['job']
    order.product = request.form['product']
    gross = request.form['gross']
    tare = request.form['tare']
    # changes gross and tare into floats
    order.gross = float(gross)
    order.tare = float(tare)
    
    # calculates net and tare, and convrs tons
    order.net = order.gross - order.tare
    order.tons = order.net / 2000

    # commits change to database
    db.session.commit()
    
    # redirects to view all orders page
    return redirect(url_for("viewOrders"))

# Delete Method
@app.route("/deleteOrder/<int:orderId>", methods=["POST"])
def deleteOrder(orderId):
    # Request OrderID, and finds it in the database
    order = Orders.query.get(orderId)
    # returns order to the delete confronfirmation page
    return render_template("delete.html", orderId = orderId)

# Delete Confirmed
@app.route("/confirmDelete", methods=["POST"])
def confirmDelete():
    # Gets the order sent from confirmation page
    orderId = request.form["orderId"]
    # finds it in the database
    order = Orders.query.get(orderId)
    # Deletes from database
    db.session.delete(order)
    # commits the database command
    db.session.commit()
    # returns to view all
    return redirect(url_for("viewOrders"))

# Method used to generate random number to be displayed
# Will be read from the Arduino Scale once implemented
@app.route('/live-data')
def data():
    # generates a random number
    data = random.randint(75000, 80000)
    
    # Makes random number into json format
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'

    #submits number to page
    return response

# run on localhost ports
if __name__ == "__main__":
    app.run(host="127.0.0", port=5000, debug=True)