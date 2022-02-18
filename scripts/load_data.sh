#!/bin/bash

source src/datasets/mysql/credentials/cred.cred

dataset_path='data/all/'


#load data sources
echo '##################### Uploading data on database ##################'
find data/datasets/ -name '*.csv' -exec cp -t data/all/ {} +
python src/datasets/mysql/csv2dbs.py --host=$host --port=$port --pwd=$pwd --uname=$uname --dbname=$dbname -i=$dataset_path