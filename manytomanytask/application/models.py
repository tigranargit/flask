from application import db

class Orders(db.Model):
    oid = db.Column(db.Integer, primary_key = True)
    products = db.relationship('OrderProducts', backref = 'orders' )

class Products(db.Model):
    pid = db.Column(db.Integer, primary_key = True)
    orders = db.relationship('OrderProducts', backref = 'products' )

class OrderProducts(db.Model):
    opid = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.oid'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.pid'))