import mysql.connector as mysql
import pandas as pd
from os import listdir
from os.path import isfile, join, splitext
from sqlalchemy import create_engine
from sqlalchemy import engine as eng
import ntpath
import sys

from arg_parser import argumentParser

# file = os.path.join(path + fileName)


def getfilesList(path):
    file_path_list = [
        join(path, f)
        for f in listdir(path)
        if isfile(join(path, f)) and (f.endswith(".csv") or f.endswith(".xlsx"))
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
    # print(db)
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


def get_file_type(filename):
    if splitext(filename)[1] == ".csv":  # csv
        return ".csv"
    elif splitext(filename)[1] == ".xlsx":  # xlsx
        return ".xlsx"
    else:
        return None


def get_no_skiprows(filename):
    skiprows = 0
    if "emdat_public" in filename:
        skiprows = 6
    return skiprows


def get_data_from_file(filename, file):
    if get_file_type(filename) == ".csv":
        data = pd.read_csv(
            file, delimiter=",", infer_datetime_format=True, encoding="utf-8"
        )
    if get_file_type(filename) == ".xlsx":
        data = pd.read_excel(file, parse_dates=True, skiprows=get_no_skiprows(filename))

    return data


def df_to_db(path, con):
    file_path_list = getfilesList(path)

    if len(file_path_list) == 0:
        print("Error: No file list to upload or wrong path")
        sys.exit()

    for file, filename in zip(
        file_path_list, [path_leaf(path) for path in file_path_list]
    ):
        try:
            data = get_data_from_file(filename, file)

            if data.empty:
                print("Error: file {} format error".format(filename))
            elif isinstance(con, eng.base.Engine):
                # print("Class Type detected :sqlalchemy.engine.base.Engine ")
                data.to_sql(
                    splitext(filename)[0], con=con, index=False, if_exists="fail"
                )
                print(
                    "Info: uploaded file {} to the mysql database successfully".format(
                        filename
                    )
                )
                # print([(i, j) for i, j in zip(data.columns, data.dtypes)])
        except Exception as e:
            print("Error: Couldn't upload file {} to the mysql".format(filename))
            print("Error: df_to_db: {}".format(e))


def upload_csvdata(file, cursor):
    pass


def engine_execution(host, port, uname, pwd, dbname, inpath):
    engine = connect_to_db(host, port, uname, pwd, dbname)
    df_to_db(inpath, engine)


def cursor_exectcution(host, port, uname, pwd, dbname, inpath):
    db = connect_to_db_mysql_con(host, port, uname, pwd, dbname)
    cursor = db.cursor()
    df_to_db(inpath, cursor)

    try:
        create_tables(cursor)
    except mysql.errors.ProgrammingError:
        print("Table already exists")
    except Exception as e:
        print("Error: cursor_exectcution {}".format(e))

    cursor.execute("SHOW TABLES")
    print("\n all tables in database", cursor.fetchall())
    db.commit()
    db.close()


def main():
    args = argumentParser()

    try:
        engine_execution(
            args.host, args.port, args.uname, args.pwd, args.dbname, args.inpath
        )

        cursor_exectcution(
            args.host, args.port, args.uname, args.pwd, args.dbname, args.inpath
        )
    except Exception as e:
        print("Error: Main: {}".format(e))


if __name__ == "__main__":
    main()
