import psycopg2
import sys

# Parámetros de conexión a la base de datos interna de pgAdmin
conn_string = "dbname='pgadmin4' user='pgadmin' host='localhost' password='admin'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

# Información de la conexión a la base de datos
server_group_id = 1
server_name = "TimescaleDB Server"
server_comment = "Connection to TimescaleDB"
connection_host = "timescaledb"
connection_port = "5432"
connection_dbname = "mydatabase"
connection_username = "timescaledb"
connection_password = "password"

try:
    insert_query = f"""
    INSERT INTO server (
        user_id, servergroup_id, name, comment, host, port, maintenance_db, username, password, ssl_mode
    ) VALUES (
        1, {server_group_id}, '{server_name}', '{server_comment}', '{connection_host}',
        {connection_port}, '{connection_dbname}', '{connection_username}',
        '{connection_password}', 'prefer'
    );
    """
    cursor.execute(insert_query)
    conn.commit()
except Exception as e:
    print(f"Error: {str(e)}", file=sys.stderr)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
