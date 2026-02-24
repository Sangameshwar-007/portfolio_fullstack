import pymysql

# Connection details (without database name)
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password=''
)

try:
    with connection.cursor() as cursor:
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS local_portfolio")
    connection.commit()
    print("Database 'local_portfolio' created or already exists.")
finally:
    connection.close()
