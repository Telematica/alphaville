#!/bin/sh -e

echo "Creating database..."

CONTAINER="rdbms_vales"
DATABASE=postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$CONTAINER:$POSTGRES_PORT

echo "CREATE DATABASE $POSTGRES_DB "| psql $DATABASE?sslmode=disable

echo "Creating schemas..."
psql $DATABASE/$POSTGRES_DB?sslmode=disable < /migrations/schema.sql

echo "Creating store procedures..."
psql  $DATABASE/$POSTGRES_DB?sslmode=disable < /migrations/stores.sql

echo "Populating tables..."
psql  $DATABASE/$POSTGRES_DB?sslmode=disable < /migrations/populate.sql
