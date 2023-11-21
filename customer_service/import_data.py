import json
from flask import Flask
from src.models import Customer
from src.main import mongo

app = Flask(__name__)

# Define a more descriptive filename
FILE_NAME = 'customer_data.json'
# print(mongo)
def import_customer_data_from_file():
    try:
        # Open the JSON file
        with open(FILE_NAME, 'r') as file:
            data = json.load(file)
            
        collection = mongo.db.actor

        for record in data:
            customer = Customer(
                first_name=record.get('first_name'),
                middle_name=record.get('middle_name'),
                last_name=record.get('last_name'),
                age=record.get('age'),
                nationality=record.get('nationality'),
                sex=record.get('sex'),
                income=record.get('income'),
                education_level=record.get('education_level'),
                position=record.get('position')
            )
            collection.insert_one(record)


    except Exception as e:
        # Log the error and print a message to the user
        print(e)
        print('Error importing customer data from file.')

if __name__ == '__main__':
    # Call the function to import data
    import_customer_data_from_file()
