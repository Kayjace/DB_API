import yaml
import mysql.connector
from pymongo import MongoClient
import datetime
import decimal
import os

def load_config():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, '../../config/config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def get_mysql_schema(cursor, table_name):
    cursor.execute(f"DESCRIBE `{table_name}`")
    return {row['Field']: {'type': row['Type'], 'nullable': row['Null'] == 'YES', 'key': row['Key']} for row in cursor.fetchall()}

def transform_schema(mysql_schema):
    # Implementation as in the original script
    pass

def transform_row(row):
    # Implementation as in the original script
    pass

def migrate_data(source_db, target_db):
    config = load_config()
    mysql_db = None
    mongo_client = None
    
    try:
        # MySQL connection
        mysql_db = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=source_db
        )
        cursor = mysql_db.cursor(dictionary=True)

        # MongoDB connection
        mongo_client = MongoClient(config['mongodb']['uri'])
        mongo_db = mongo_client[target_db]

        for table in config['tables']:
            source_table = table['mysql_table']
            target_collection = table['mongo_collection']
            collection = mongo_db[target_collection]

            mysql_schema = get_mysql_schema(cursor, source_table)
            mongo_schema = transform_schema(mysql_schema)

            cursor.execute(f"SELECT * FROM `{source_table}`")
            
            chunk_size = 1000
            inserted_count = 0
            while True:
                rows = cursor.fetchmany(chunk_size)
                if not rows:
                    break
                transformed_rows = [transform_row(row) for row in rows]
                collection.insert_many(transformed_rows)
                inserted_count += len(rows)

            print(f"Migrated {inserted_count} records from {source_table} to {target_collection}")

        return {"message": "Migration completed successfully"}

    except Exception as e:
        print(f"Error during migration: {e}")
        return {"error": str(e)}

    finally:
        if mysql_db:
            mysql_db.close()
        if mongo_client:
            mongo_client.close()