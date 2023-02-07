from flask import Flask, render_template, make_response, url_for, request, redirect
from datetime import datetime

from sqlalchemy import DECIMAL
from flask_sqlalchemy import SQLAlchemy

import requests
import json
import random
# import DataService

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/mtz-materials'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

app.app_context().push()

tare = 0

class Orders(db.Model):
    orderId = db.Column(db.Integer, primary_key=True)
    truckId = db.Column(db.String(80), unique=False, nullable=False)
    truckCo = db.Column(db.String(80), unique=False, nullable=False)
    customer = db.Column(db.String(80), unique=False, nullable=False)
    job = db.Column(db.String(80), unique=False, nullable=False)
    product = db.Column(db.String(80), unique=False, nullable=False)
    gross = db.Column(DECIMAL(7,2), unique=False, nullable=False)
    tare = db.Column(DECIMAL(7,2), unique=False, nullable=False)
    net = db.Column(DECIMAL(7,2), unique=False, nullable=False)
    tons = db.Column(DECIMAL(7,2), unique=False, nullable=False)

    def __repr__(self):
        return '<Order %r>' % self.orderId
    


    # app name
@app.errorhandler(404)
  
# inbuilt function which takes error as parameter
def not_found(e):
# defining function
  return render_template("404.html")

@app.route("/")
def index():
    gross = data().json
    return render_template('index.html', gross = gross)

@app.route("/createOrder")
def createOrder():
    return render_template('inputTare.html')


@app.route("/createOrderForm", methods=['POST', 'GET'])
def createOrderForm():
    
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
                newOrder = Orders(truckId = truckId, truckCo = truckCo, customer = customer, job= job, product = product, gross = gross, tare = tare, net= net, tons = tons)
                db.session.add(newOrder)
                db.session.commit()
                return render_template('index.html')
            except Exception as e:
                print(e)
             
                return 'There was an issue creating your Order'

        else:
            inTare = request.args.get("inTare")
            tare = float(inTare)
            net = data().json - tare         
            tons = net / 2000
            return render_template('createOrder.html', gross = data().json, tare = tare, net = net, tons = ("{:.2f}".format(tons)))



@app.route("/viewOneOrder/<int:orderId>", methods=['GET','POST'])
def viewOneOrder(orderId):
    if request.method == 'POST':

        order = Orders.query.get(orderId)

        return render_template('updateOrder.html', order = order)
    else:
        return redirect('/viewOrders')


@app.route("/viewOrders")
def viewOrders():
    orderList = Orders.query.all()
    return render_template('viewOrders.html', orderList = orderList)

@app.route("/updateOrder", methods=["POST"])
def updateOrder():

    orderId = request.form['orderId']

    order = Orders.query.get(orderId)
    
    order.truckId = request.form['truckId']
    order.truckCo = request.form['truckCo']
    order.customer = request.form['customer']
    order.job = request.form['job']
    order.product = request.form['product']

    gross = request.form['gross']
    tare = request.form['tare']
    order.gross = float(gross)
    order.tare = float(tare)
    order.net = order.gross - order.tare
    order.tons = order.net / 2000
    net = request.form['net']
    tons = request.form['tons']
    db.session.commit()
    
    return redirect(url_for("viewOrders"))


@app.route("/deleteOrder/<int:orderId>", methods=["POST"])
def deleteOrder(orderId):

    order = Orders.query.get(orderId)
    
    return render_template("delete.html", orderId = orderId)

@app.route("/confirmDelete", methods=["POST"])
def confirmDelete():
    orderId = request.form["orderId"]
    order = Orders.query.get(orderId)
    print(order)
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for("viewOrders"))

@app.route('/live-data')
def data():
    data = random.randint(75000, 80000)
    
    # Loads data that can then be read
    #data = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
    #print(data['two'])  # or `print data['two']` in Python 2

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response




if __name__ == "__main__":
    app.run(host="127.0.0", port=5000, debug=True)