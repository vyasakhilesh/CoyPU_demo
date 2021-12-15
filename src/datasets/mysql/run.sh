#!/bin/bash

source src/datasets/mysql/credentials/cred.cred

python db/csv2dbs.py --host=$host --port=$port --pwd=$pwd --uname=$uname --dbname=$dbname -i='data/datasets'

