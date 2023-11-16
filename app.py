from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '6e285583f6b41cbfc917a6913543123c'
db = SQLAlchemy(app)

# Define the Booking Model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    coupon = db.Column(db.String(20), unique=True)

# Function to create tables if they do not exist
def create_tables():
    with app.app_context():
        db.create_all()

# Run the function to create tables
create_tables()

# Landing Page Route
@app.route('/')
def landing():
    return render_template('landing.html')

# Index Page Route
@app.route('/index')
def index():
    return render_template('index.html')

# Checkout Page Routes
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        
        # Save booking details to the database
        new_booking = Booking(name=name, address=address)
        db.session.add(new_booking)
        db.session.commit()

        return render_template('checkout_success.html', name=name, address=address)

    return render_template('checkout.html')

@app.route('/checkout/success')
def checkout_success():
    return render_template('checkout_success.html')

# Restaurant Registration Routes
@app.route('/restaurant/register', methods=['GET', 'POST'])
def restaurant_register():
    if request.method == 'POST':
        # Retrieve restaurant registration details from form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Create a new restaurant record and add to the database
        new_restaurant = Restaurant(username=username, email=email, password=password)
        db.session.add(new_restaurant)
        db.session.commit()

        # Optionally, redirect to a login page after successful registration
        return render_template('restaurant_login.html')

    return render_template('restaurant_register.html')

# Restaurant Login Routes
@app.route('/restaurant/login', methods=['GET', 'POST'])
def restaurant_login():
    if request.method == 'POST':
        # Retrieve username and password from the login form
        username = request.form['username']
        password = request.form['password']

        # Check authentication with the Restaurant model
        # Add logic to verify credentials and manage sessions
        
    return render_template('restaurant_login.html')

if __name__ == '__main__':
    app.run(debug=True)