from flask import redirect,render_template,url_for,flash,request
from shop.products.models import Brand,Category
from shop import db,app

@app.route('/addbrand',methods=['GET','POST'])
def addbrand():
    return render_template('products/addbrand.html')

@app.route('/createdb')
def createdb():
    db.create_all()
    return "data base created"
