#!/bin/bash

# Replace the following variables with your actual credentials

MYSQL_USER="root"
MYSQL_PASSWORD="root"

# Execute the MYSQL command to list databases
mysql -h localhost -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e
"SHOW DATABASES;"
