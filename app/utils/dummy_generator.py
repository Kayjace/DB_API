import random
import string
from datetime import datetime, timedelta
import sqlalchemy as db

def generate_dummy_value(data_type):
    if 'int' in data_type.lower():
        return random.randint(1, 1000)
    elif 'varchar' in data_type.lower():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    elif 'date' in data_type.lower():
        return (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
    elif 'time' in data_type.lower():
        return f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
    elif 'text' in data_type.lower():
        return ' '.join(''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 10))) for _ in range(20))
    else:
        return None

def generate_data(table_name, num_records):
    # This function should use the table schema to generate appropriate dummy data
    # You'll need to implement the logic to fetch the table schema and generate data accordingly
    pass

#더미데이터를 삽입
def insert_data(selected_table, metadata, engine, data):
    table = db.Table(selected_table, metadata, autoload=True, autoload_with=engine)
    insert_num = 0
    #데이터가 존재하지 않는다면
    if not data:
        print("삽입할 데이터가 없습니다.")
        return
    with engine.connect() as conn:
        with conn.begin():
            for d in data:
                try:
                    query = table.insert().values(d)
                    conn.execute(query)
                    insert_num += 1
                except Exception as e:
                    continue
    if insert_num == 0:
        print("제약조건으로 인해 데이터를 더 추가할 수 없습니다.")
    else:
        print(f"{insert_num}개의 데이터를 {selected_table}에 넣었습니다.")