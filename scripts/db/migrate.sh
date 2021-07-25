#!/bin/bash

MIGRATION_DIR="db/migrations"
DB_FILE="db/main.db"

for migration_file in "${MIGRATION_DIR}"/*.up.sql; do
    printf "running migration '%s'\n" "${migration_file}"
    sqlite3 "${DB_FILE}" < "${migration_file}"
done 
