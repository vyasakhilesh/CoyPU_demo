import mysql.connector as mysql
import csv
import pandas as pd
from os import listdir
from os.path import isfile, join, splitext
from sqlalchemy import create_engine
from sqlalchemy import engine as eng
import ntpath

from arg_parser import argumentParser

# file = os.path.join(path + fileName)


def getfilesList(path):
    file_path_list = [
        join(path, f)
        for f in listdir(path)
        if isfile(join(path, f)) and f.endswith(".csv")
    ]
    return file_path_list


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def connect_to_db_mysql_con(host, port, uname, pwd, dbname):
    db = mysql.connect(
        host=host,
        port=port,
        user=uname,
        passwd=pwd,
        database=dbname,
    )
    print(db)
    return db


def connect_to_db(host, port, uname, pwd, dbname):
    engine = create_engine(
        "mysql+pymysql://{user}:{pw}@{hostname}:{portno}/{db}".format(
            hostname=host, db=dbname, user=uname, pw=pwd, portno=port
        )
    )
    return engine


def create_tables(cursor):
    # cursor.execute("CREATE TABLE test (name VARCHAR(255), user_name VARCHAR(255))")
    pass


def df_to_db(path, con):
    file_path_list = getfilesList(path)
    # print(file_path_list)

    for file, filename in zip(
        file_path_list, [path_leaf(path) for path in file_path_list]
    ):
        data = pd.read_csv(
            file, delimiter=",", infer_datetime_format=True, encoding="utf-8"
        )

        if isinstance(con, eng.base.Engine):
            print("Class Type detected :sqlalchemy.engine.base.Engine ")
            data.to_sql(
                splitext(filename)[0], con=con, index=False, if_exists="replace"
            )

        print([(i, j) for i, j in zip(data.columns, data.dtypes)])


def upload_csvdata(file, cursor):
    pass


def engine_execution(host, port, uname, pwd, dbname, inpath):
    engine = connect_to_db(host, port, uname, pwd, dbname)
    df_to_db(inpath, engine)


def cursor_exectcution(host, port, uname, pwd, dbname, inpath):
    db = connect_to_db_mysql_con(host, port, uname, pwd, dbname)
    cursor = db.cursor()
    # cursor.execute("SHOW DATABASES")
    # print("all databases", cursor.fetchall())
    df_to_db(inpath, cursor)

    try:
        create_tables(cursor)
    except mysql.errors.ProgrammingError:
        print("Table already exists")

    cursor.execute("SHOW TABLES")
    print("all tables", cursor.fetchall())
    db.commit()
    db.close()


def main():
    args = argumentParser()
    engine_execution(
        args.host, args.port, args.uname, args.pwd, args.dbname, args.inpath
    )
    cursor_exectcution(
        args.host, args.port, args.uname, args.pwd, args.dbname, args.inpath
    )


if __name__ == "__main__":
    main()
