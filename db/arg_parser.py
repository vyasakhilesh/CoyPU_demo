import argparse


def argumentParser():
    parser = argparse.ArgumentParser(description="Convert CSVFiles to DB")
    parser.add_argument(
        "-i",
        "--inpath",
        type=str,
        required=True,
        action="store",
        help="inpath csv files",
    )
    parser.add_argument(
        "-x",
        "--host",
        type=str,
        required=True,
        action="store",
        help="hostname",
    )
    parser.add_argument(
        "-u", "--uname", type=str, required=True, action="store", help="username"
    )
    parser.add_argument(
        "-s", "--pwd", type=str, required=True, action="store", help="passwd"
    )
    parser.add_argument(
        "-p", "--port", type=str, required=True, action="store", help="port"
    )
    parser.add_argument(
        "-d",
        "--dbname",
        type=str,
        required=True,
        action="store",
        help="db name",
    )
    return parser.parse_args()
