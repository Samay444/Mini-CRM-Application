from app import app
from flask import render_template, request, redirect, url_for, flash
from app.models import db, Customer
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/crm'
db = SQLAlchemy(app)
class Customers(db.Model):
    name = db.Column(db.VARCHAR(64), primary_key=True)
    Email = db.Column(db.VARCHAR(120), unique=True)
    Phone_num = db.Column(db.VARCHAR(12), unique=True)
    Orders = db.Column(db.VARCHAR(500), unique=False)



@app.route('/')
def index():
    customers = Customer.query.all()
    return render_template('index.html', customers=customers)

@app.route('/add', methods=['GET', 'POST'])

def add_customer():
    if request.method == 'POST':
        name = request.form.get['name']
        email = request.form.get['email']
        phone = request.form.get['phone']
        orders = request.form.get['orders']
        entry = Customers(Name=name, Email=email, Phone_num=phone, Orders=orders)
        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('index'))
    flash('Customer Added successfully', 'success')
    return render_template('add_customer.html')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_customer(id):
    customer = Customer.query.get(id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        flash('Customer deleted successfully', 'success')
    else:
        flash('Customer not found', 'error')
    return redirect(url_for('index'))

