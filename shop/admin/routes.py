from flask import redirect,session,request,render_template,url_for,flash

from .models import User
from .forms import RegistrationForm, LoginForm
from shop.products.models import Addproduct,Brand,Category

from shop import app,db,bcrypt


@app.route('/admin')
def admin():
    if 'email' not in session:
        flash('Please first login', 'danger')
        return redirect(url_for('login'))
    products=Addproduct.query.all()
    return render_template('admin/index.html', title='Admin Page' ,products=products)

@app.route('/')
def home():
    return render_template('admin/index.html',title='Admin Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username=form.username.data, email=form.email.data,password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.name.data} Thanks for registering','success')
        return redirect(url_for('login'))       # we hava pass the function name in url_for
    return render_template('admin/register.html', form=form,title='Registration page')

@app.route('/create')
def create():
    db.create_all()
    return "data base created"


@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user= User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            session['email']=form.email.data
            flash(f'Welcome {form.email.data} you are login now','success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash(f'Wrong Password please try again','danger')
        

    return render_template('admin/login.html',form=form,title='Login Page')