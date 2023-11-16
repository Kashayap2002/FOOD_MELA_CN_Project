from app import app, db  # Import Flask app and SQLAlchemy db instance
from app import Booking  # Assuming 'Booking' is your SQLAlchemy model

def create_tables():
    with app.app_context():
        # Initialize the app with the database instance
        db.init_app(app)
        # Create all tables if they don't exist
        db.create_all()

if __name__ == '__main__':
    create_tables()
