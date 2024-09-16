from app import db

def get_schema():
    # Logic to get schema from MySQL
    query = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys')"
    result = db.engine.execute(query)
    return [row[0] for row in result]

def get_tables():
    # Logic to get tables from MySQL
    query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = :schema"
    result = db.engine.execute(query, {'schema': db.engine.url.database})
    return [row[0] for row in result]