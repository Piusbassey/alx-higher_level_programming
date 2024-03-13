#!/bin/bash

# Replace the following variables with your actual MySQL credentials
MYSQL_USER="root"
MYSQL_PASSWORD="root"
DATABASE_NAME="hbtn_0c_0"

# Execute the MySQL command to create the database if it doesn't exist
mysql -h localhost -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "CREATE DATABASE IF NOT EXISTS $DATABASE_NAME;"

# Check if the database was created or already existed
if [ $? -eq 0 ]; then
	echo "DATABASE_CREATED"
else
	echo "DATABASE_EXIST"
	fi

