from flask import Flask, render_template, make_response, url_for, request, redirect, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import requests
import json
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)



class Order(db.Model):
    orderId = db.Column(db.Integer, primary_key = True)
    truckId = db.Column(db.String(200), nullable = False)
    truckCo = db.Column(db.String(200), nullable = False)
    customer = db.Column(db.String(200), nullable = False)
    job = db.Column(db.String(200), nullable = False)
    product = db.Column(db.String(200), nullable = False)
    gross = db.Column(db.Float, default=0, nullable = False)
    tare = db.Column(db.Float, default=0, nullable = False)
    net = db.Column(db.Float, default=0, nullable = False)
    tons = db.Column(db.Float, default=0, nullable = False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task &r>' % self.orderId


with app.app_context():
    db.create_all()
    db.session.commit()


tare = 30000

@app.route("/")
def index():
    return render_template('index.html', gross = data().json)

@app.route('/createOrder', methods=['POST', 'GET'])
def create():

        if request.method == 'POST':
            order_truckId = request.form['truckId']
            order_truckCo = request.form['truckCo']
            order_customer = request.form['customer']
            order_job = request.form['job']
            order_product = request.form['product']
            order_gross = request.form['gross']
            order_tare = request.form['tare']
            order_net = request.form['net']
            order_tons = request.form['tons']
            
            newOrder = Order(truckId=order_truckId, truckCo=order_truckCo, customer=order_customer, 
                                 job=order_job, product=order_product,
                                 gross=order_gross, tare=order_tare, net=order_net, tons=order_tons
                                )
            try:
                db.session.add(newOrder)
                db.session.commit()
                return redirect('/')
            except:
                return 'There was an issue creating your Order'

        else:
            net = data().json - tare
            tons = net / 2000
            return render_template('form.html', gross = data().json, tare = tare, net = net, tons = ("{:.2f}".format(tons)))


@app.route("/viewOrders")
def viewOrders():
    return render_template('viewOrder.html')

@app.route('/live-data')
def data():
    data = random.randint(75000, 80000)
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
