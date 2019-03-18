#!/usr/bin/env bash
# @c0demech // Michael Edie 20190318
#####################################################
#; Guacamole Database Initialization Schema Retriever 
#####################################################
## When you migrate your db backup (mysqldump) you need to
## initialize the new database with the same schema version
## as the backup. This script automates getting the schema
## and provides the command for mysql/postgresql in order
## to initialize the db.
#;

# Change version and database type if necessary
GUACAMOLE_VERSION=0.9.14
AUTH_JDBC_URL="http://archive.apache.org/dist/guacamole/${GUACAMOLE_VERSION}/binary/guacamole-auth-jdbc-${GUACAMOLE_VERSION}.tar.gz"
GUACAMOLE_AUTH_JDBC="guacamole-auth-jdbc-${GUACAMOLE_VERSION}.tar.gz"
# mysql or postgresql
DB_TYPE=mysql
OUTPUTDIR=/tmp
OUTPUTFILE=v${GUACAMOLE_VERSION}-initdb.sql

# Skip downloading if we find the tgz in the cwd
if [ -f $GUACAMOLE_AUTH_JDBC ]; then
   echo "$GUACAMOLE_AUTH_JDBC already downloaded. Exiting"
   exit 1
fi
# Download 
wget $AUTH_JDBC_URL

# Extract
tar xf $GUACAMOLE_AUTH_JDBC

# Generate schema for db initialization
cat guacamole-auth-jdbc-${GUACAMOLE_VERSION}/${DB_TYPE}/schema/*.sql > ${OUTPUTDIR}/${OUTPUTFILE}
echo "================== Complete ================== "
echo ""
echo "To iniitalize a new database: "

# Output for MariaDB
if [ "$DB_TYPE" = "mysql" ]; then
  echo "mysql -u root -p guacamole_db < $OUTPUTFILE"
fi

# Output for Postgres
if [ "$DB_TYPE" = "postgresql" ]; then
  echo "psql -U postgres guacamole_db -f $OUTPUTFILE"
fi

echo ""
echo "==================================== "
