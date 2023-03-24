from flask import render_template, make_response, url_for, request, redirect, abort

import pdfkit
from app import app
from app import cache

# Import Date & Time used for the connection to the Arduino (not implemented)
from datetime import datetime

# Class Model for the Databse
from app.models import Orders, db, desc, asc
# allows http requests
import requests
# used to make json format
import json
# generates random number
import random

# Serial port import
import serial
import time

cache.clear()

ser = serial.Serial()
while True:
    try: 
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
        print("Successfully connected Serial.")
        break
    except serial.SerialException:
        print("Could not connect to Serial. Try again.")       
        time.sleep(1)
        ser.close()
        break
    else:
        print(ser)

# Error handling for pages not found, 404 Error
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
# 404 Error page 
  return render_template("404.html")

@app.errorhandler(500)
# inbuilt function which takes error as parameter
def serial_not_found(e):
# 404 Error page 
  return render_template("500.html")


# Landing page used to display the weight from the scale
@app.route("/")
def index():
    # calls the 
    # if not ser.isOpen():
    #     print("Serial port Has been disconnected")

    #     abort(500)

    gross = live_data().json
    return render_template('index.html', gross = gross)

@app.route("/inputTare", methods=['POST'])
def input_tare():
    gross = request.form['gross']
    return render_template('inputTare.html', gross = gross)

# Create Order Method, Returns Create Order page
@app.route("/createOrder", methods=['POST'])
def create_order():
    gross = request.form['gross']
    tare = request.form['tare']
    # converts message into a float
    gross = float(gross)
    tare = float(tare)
            
    # calculates the net using the gross weight from reading the scale
    net = gross - tare         

    # generates tons 
    tons = net / 2000
    return render_template('createOrder.html', gross = gross, tare = tare, net = net, tons = ("{:.2f}".format(tons)))

# Create Order method, GET method displays page, POST submits the form
@app.route("/createOrderForm", methods=['POST'])
def create_order_form():
        # If form is submitted, read all the properties
        # if request.method == 'POST':
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
            return redirect(url_for("index"))
            #General exception handler
        except Exception as e:
            # print error
            print(e)
            return 'There was an issue creating your Order'

# View all orders
@app.route("/viewOrders")
def view_orders():
    # selects all orders from database
    orderList = Orders.query.order_by(desc(Orders.orderId)).all()
    # returns view all order page and list of orders
    return render_template('viewOrders.html', orderList = orderList)

# View all orders
@app.route("/viewOrdersProduct")
def view_orders_product():
    # selects all orders from database
    orderList = Orders.query.group_by(Orders.product).order_by(desc(Orders.product)).all()
    # returns view all order page and list of orders
    return render_template('viewOrders.html', orderList = orderList)


# Update Order Page
@app.route("/updateOrder", methods=["POST"])
def update_order():

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
    return redirect(url_for("view_orders"))

# Delete Method
@app.route("/deleteOrder/<int:orderId>", methods=["POST"])
def delete_order(orderId):
    # Request OrderID, and finds it in the database
    order = Orders.query.get(orderId)
    # returns order to the delete confronfirmation page
    return render_template("delete.html", orderId = orderId)

# Delete Confirmed
@app.route("/confirmDelete", methods=["POST"])
def confirm_delete():
    # Gets the order sent from confirmation page
    orderId = request.form["orderId"]
    # finds it in the database
    order = Orders.query.get(orderId)
    # Deletes from database
    db.session.delete(order)
    # commits the database command
    db.session.commit()
    # returns to view all
    return redirect(url_for("view_orders"))

# Method used to generate random number to be displayed
# Will be read from the Arduino Scale once implemented
@app.route('/live-data')
def live_data():
    # if not ser.isOpen():
    #     abort(500)
    # generates a random number
    data = random.randint(75000, 80000)
    
    # Makes random number into json format
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    
    #submits number to page
    return response

