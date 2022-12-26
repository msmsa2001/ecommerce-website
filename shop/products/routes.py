from flask import redirect,render_template,url_for,flash,request,session
from shop.products.models import Brand,Category,Addproduct
from shop import db,app
from .forms import Addproducts

@app.route('/addbrand',methods=['GET','POST'])
def addbrand():
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    if request.method=='POST':
        getbrand=request.form.get('brand')
        brand=Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The Brand {getbrand} was added to your  database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html',brands='brands')

@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    if request.method=='POST':
        getbrand=request.form.get('brand')
        brand=Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The Brand {getbrand} was added to your  database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html',brands='brands')

@app.route('/updatecat/<int:id>',methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash(f'Please login first','danger')
    updatecat=Category.query.get_or_404(id)
    category=request.form.get('category')
        # return redirect(url_for('login'))
    if request.method=='POST':
        updatecat.name=category
        flash(f'The Brand {updatecat} was added to your  database','success')
        # db.session.add(brand)
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('products/updatebrand.html',updatecat=updatecat)

@app.route('/addcat',methods=['GET','POST'])
def addcat():
    if request.method=='POST':
        getcat=request.form.get('category')
        cat=Category(name=getcat)
        db.session.add(cat)
        flash(f'The Category {getcat} was added to your  database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html')



@app.route('/addproduct',methods=['GET','POST'])
def addproduct():
    form=Addproducts(request.form)
    return render_template('products/addproducts.html',title='Add products page',form=form)

@app.route('/createdb')
def createdb():
    db.create_all()
    return "data base created"
