import mysql.connector as mysql
import csv
import argparse as ap
import pandas as pd
import os
from sqlalchemy import create_engine

path = "/home/tibvyasa/projects/proj_off/data_off/coypu/ips/data/"
fileName = "CountryData2021.csv"
file = os.path.join(path + fileName)

# Credentials to database connection
hostname = "localhost"
dbname = "mydb_name"
uname = "my_user_name"
pwd = "my_password"
port = "port"


def connect_to_db():
    db = mysql.connect(
        host=hostname,
        port=port,
        user=uname,
        passwd=pwd,
        database=dbname,
    )
    print(db)
    return db


def create_tables(cursor):
    cursor.execute("CREATE TABLE test (name VARCHAR(255), user_name VARCHAR(255))")
    cursor.execute("CREATE TABLE test (name VARCHAR(255), user_name VARCHAR(255))")


def file_dtypes_details(file, cursor):
    data = pd.read_csv(
        file, delimiter=",", infer_datetime_format=True, encoding="utf-8"
    )
    data.to_sql("users", con=cursor)
    print([(i, j) for i, j in zip(data.columns, data.dtypes)])


def upload_csvdata(file, cursor):
    pass


def main():
    db = connect_to_db()
    print(db)
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")
    print("all databases", cursor.fetchall())
    file_dtypes_details(file, cursor)

    try:
        create_tables(cursor)
    except mysql.errors.ProgrammingError:
        print("Table already exists")

    cursor.execute("SHOW TABLES")
    print("all tables", cursor.fetchall())
    db.commit()
    db.close()


if __name__ == "__main__":
    main()
