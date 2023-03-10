from flask import redirect,render_template,url_for,flash,request,session
from shop.products.models import Brand,Category,Addproduct
from shop import db,app,photos
from .forms import Addproducts
import secrets

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
        return redirect(url_for('addbrands'))
    return render_template('products/addbrand.html',brands='brands')

@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    updatebrand=Brand.query.get_or_404(id)
    if request.method=='POST':
        getbrand=request.form.get('brand')
        updatebrand.name=getbrand
        # brand=Brand(name=getbrand)
        # db.session.add(brand)
        flash(f'The Brand {getbrand} was added to your  database','success')
        db.session.commit()
        return redirect(url_for('brand'))
    return render_template('products/updatebrand.html',updatebrand=updatebrand,title='Update Brand page')

@app.route('/updatecat/<int:id>',methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    updatecat=Category.query.get_or_404(id)
        # return redirect(url_for('login'))
    if request.method=='POST':
        category=request.form.get('category')
        updatecat.name=category
        flash(f'The Brand {updatecat} was added to your  database','success')
        # db.session.add(brand)
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('products/updatebrand.html',updatecat=updatecat )

@app.route('/addcat',methods=['GET','POST'])
def addcat():
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
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
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    brands=Brand.query.all()
    categories=Category.query.all()
    form=Addproducts(request.form)
    if request.method=='POST':
        name=form.name.data
        price=form.price.data
        discount=form.discount.data
        stock=form.stock.data
        colors=form.colors.data
        desc=form.discription.data
        brand=request.form.get('brand')
        category=request.form.get('category')
        image_1=photos.save(request.files.get('image_1'),name=secrets.token_hex(10)+".")
        image_2=photos.save(request.files.get('image_2'),name=secrets.token_hex(10)+".")
        image_3=photos.save(request.files.get('image_3'),name=secrets.token_hex(10)+".")
        addpro=Addproduct(name=name,price=price,discount=discount,stock=stock,colors=colors,desc=desc,brand_id=brand,category_id=category,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(addpro)
        flash(f'the product {name} has been added to your database','success')
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('products/addproducts.html',title='Add products page',form=form,brands=brands,categories=categories)


@app.route('/updateproduct/<int:id>',methods=['POST','GET'])
def updateproduct(id):
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    brands=Brand.query.all()
    categories=Category.query.all()
    updateProduct=Addproduct.query.get_or_404(id)
    brand=request.form.get('brand')
    category=request.form.get('category')
    form=Addproducts(request.form)
    if request.method == 'POST':
        updateProduct.name=form.name.data
        updateProduct.price=form.price.data
        updateProduct.discount=form.discount.data
        updateProduct.brand_id=brand
        updateProduct.category_id=category
        updateProduct.colors=form.colors.data
        updateProduct.desc=form.discription.data
        flash(f'the product has been updated to your database','success')
        db.session.commit()
        return redirect(url_for('admin'))


    form.name.data=updateProduct.name
    form.price.data=updateProduct.price
    form.discount.data=updateProduct.discount
    form.stock.data=updateProduct.stock
    form.colors.data=updateProduct.colors
    form.discription.data=updateProduct.desc
    
    # photos.save(request.files.get('image_1'),name=secrets.token_hex(10)+".")
    # photos.save(request.files.get('image_2'),name=secrets.token_hex(10)+".")
    # photos.save(request.files.get('image_3'),name=secrets.token_hex(10)+".")
    return render_template('products/updateproduct.html',form=form,updateProduct=updateProduct,brands=brands,categories=categories)
    



@app.route('/createdb')
def createdb():
    db.create_all()
    return "data base created"
