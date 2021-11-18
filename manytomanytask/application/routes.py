from application import app, db
from application.models import OrderProducts, Orders, Products


@app.route('/addorders')

def addorders():
    neworder = Orders()
    db.session.add(neworder)
    db.session.commit()
    return "New order added to database"

@app.route('/addproducts')

def addprods():
    newproduct = Products()
    db.session.add(newproduct)
    db.session.commit()
    return "New product added to database"  

@app.route('/neworderproduct/<int:oid>-<int:pid>')

def addorderprod(oid,pid):
    neworderproduct = OrderProducts(order_id=oid, product_id=pid)
    db.session.add(neworderproduct)
    db.session.commit()
    return "New orderproduct added to databse"

@app.route('/view-orders')

def view_orders():
    orders = Orders.query.all()
    ostring = ''
    for order in orders:
        orderprods = OrderProducts.query.filter_by(order_id=order.oid).all()
        prods = [str(Products.query.get(p.product_id).pid) for p in orderprods]
        ostring += '<br>' + str(order.oid) + ':' + ', '.join(prods)
    return ostring


