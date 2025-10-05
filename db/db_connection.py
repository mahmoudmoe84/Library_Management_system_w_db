import mysql.connector
from mysql.connector import Error
from .config import settings
def get_connection():
    return mysql.connector.connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_DATABASE
    )

def get_db_schema():
    """_summary_
    reterieves databse schema from mysql to provide context to the llm
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SHOW TABLES;')
        tables = [table[0] for table in cur.fetchall()]
        schema_parts=[]
        for table_name in tables:
            cur.execute(f"SHOW CREATE TABLE {table_name}")
            create_statement = cur.fetchone()[1]
            schema_parts.append(create_statement)
        return "\n\n".join(schema_parts)
    except Error as e:
        print(f"Error getting shcmea from mysql {e}")
        return None
    finally:
        if conn and conn.is_connected():
            cur.close()
            conn.close()
            
def execute_read_query(query:str):
    """
    _summary_
    execute read-only (select) on mysql and returns the results
    """
    if not query.strip().upper().startswith('SELECT'):
        print('Security warning only select queries are allow for this feature')
        return None
    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute(query)
        results = cur.fetchall()
        return results
    except Error as e:
        print(f'mysqla database error {e}')
    finally:
        if conn and conn.is_connected():
            cur.close()
            conn.close