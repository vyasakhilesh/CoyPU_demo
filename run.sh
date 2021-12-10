source ./db/cred.cred
dataset_path=''


python db/csv2dbs.py --host=$host --port=$port --pwd=$pwd --uname=$uname --dbname=$dbname -i=$dataset_path


