export PGPASSWORD=qwerty12
psql --host 127.0.0.1 -p 5431 -U postgres -d postgres -c "drop database netology_fastapi_db"
psql --host 127.0.0.1 -p 5431 -U postgres -d postgres -c "create database netology_fastapi_db"