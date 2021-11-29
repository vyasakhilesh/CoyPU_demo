#!/bin/bash

source ./db/cred.cred


python db/csv2dbs.py --host=$host --port=$port --pwd=$pwd --uname=$uname --dbname=$dbname -i='/home/tibvyasa/projects/proj_off/data_off/coypu/ips/data/'

