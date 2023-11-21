import os
from flask import Flask
from routes import customer_bp
from models import mongo, Customer
from dotenv import load_dotenv
import sys
sys.path.append("src")


load_dotenv()


app = Flask(__name__)


mongoUsername = os.getenv("mongoUsername")
mongoPassword = os.getenv("mongoPassword")

# Set up MongoDB connection
app.config['MONGO_URI'] = f"mongodb+srv://{mongoUsername}:{mongoPassword}@tm-dev-cluster.4xzve.mongodb.net/actor?retryWrites=true&w=majority"

mongo.init_app(app)

# Register the customer blueprint
app.register_blueprint(customer_bp)


if __name__ == '__main__':
    app.run(debug=True)
