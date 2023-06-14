from postgres_db import db_connector

def startup_database():
    # drop_tables()
    create_tables_if_neded()

# Database structure =======================================================================================================================

def create_tables_if_neded():
    create_list_table_if_needed()
    create_list_items_table_if_needed()


def create_list_table_if_needed():
    conn = db_connector()
    cursor = conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS public.lists (
        name varchar(64) UNIQUE,
        footNote varchar(128) NULL
    );'''
    cursor.execute(sql)
    conn.commit()
    conn.close()


def create_list_items_table_if_needed():
    conn = db_connector()
    cursor = conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS public.list_items (
        name varchar(64),
        note varchar(256) NULL,
        list varchar(64)
    );'''
    cursor.execute(sql)
    conn.commit()
    conn.close()

# Drop Tables ==============================================================================================================================
def drop_tables():
    dropListsTable()
    dropItemsTable()

def dropItemsTable():
    conn = db_connector()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS public.list_items")
    conn.commit()
    conn.close()


def dropListsTable():
    conn = db_connector()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS public.lists")
    conn.commit()
    conn.close()