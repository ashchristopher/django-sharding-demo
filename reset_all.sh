#! /bin/bash

echo "**** Dropping databases ****"
mysql -uroot -e "drop database multidb_main"
mysql -uroot -e "drop database multidb_accounts"
mysql -uroot -e "drop database multidb_shard1"
mysql -uroot -e "drop database multidb_shard2"
mysql -uroot -e "drop database multidb_shard3"

echo "**** Creating databases ****"
mysql -uroot -e "create database multidb_main"
mysql -uroot -e "create database multidb_accounts"
mysql -uroot -e "create database multidb_shard1"
mysql -uroot -e "create database multidb_shard2"
mysql -uroot -e "create database multidb_shard3"

echo "--- syncing default ---"
python manage.py syncdb --noinput
echo
echo "--- syncing accounts ---"
python manage.py syncdb --noinput --database=accounts
echo
echo "--- syncing shard0 ---"
python manage.py syncdb --noinput --database=shard0
echo
echo "--- syncing shard1 ---"
python manage.py syncdb --noinput --database=shard1
echo
echo "--- syncing shard2 ---"
python manage.py syncdb --noinput --database=shard2
echo
echo "Creating superuser"
python manage.py createsuperuser --username=admin --email=admin@example.com 
