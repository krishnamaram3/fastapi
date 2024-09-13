import mysql.connector
import datetime
import time
import os

def mysql_connect():
    # Establish a connection to the MySQL database
    db_con = mysql.connector.connect(
        host=os.environ['DB_SERVER'],
        user=os.environ['DB_USR'],
        password=os.environ['DB_PWD'],
    )
    return db_con

def get_all_stones():
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    # Execute a SELECT query
    query = f"SELECT * FROM csit.cloud_stones"
    db_session.execute(query)

    # Fetch all records from the result set
    all_stones = db_session.fetchall()
    # import time
    # print("records", records)
    # Fetch column names from the cursor description
    # column_names = [desc[0] for desc in db_session.description]
    # Process the fetched data
    stones = []
    for stone in all_stones:
        stone_dict = {
            "stone_id" : stone[0],
            'cloud_provider': stone[1],
            'cloud_account': stone[2],
            'region': stone[3],
            'stones_status': stone[4]
        }
        stones.append(stone_dict)
    print(stones)
    return stones