from app.utils.dummy_generator import generate_data
from app.utils.dummy_generator import insert_data

def generate_dummy_data(data):
    # Use the generate_data function from dummy_generator.py
    return generate_data(data['table_name'], data['num_records'])

def insert_dummy_data(data):
    # Use the insert_data function from db_utils.py
    return insert_data(data['table_name'], data['records'])