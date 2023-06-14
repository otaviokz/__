from postgres_db import db_connector
import sys

# Lists ====================================================================================================================================
def fetch_lists():
    conn = db_connector()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.lists")
    result = []
    for row in cursor.fetchall():
        result.append( { 
            "name": row[0],
            "footNote": row[1]
        })
    conn.commit()
    cursor.close()
    conn.close()
    return result


def add_list(name, footNote):
    if listAlreadyExists(name):
        return {"type": "failure", "message": "List {} already exists.".format(name)}
    else:
        conn = db_connector()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO public.lists (name, footNote) VALUES(%s, %s)", (name, footNote,))
        conn.commit()
        cursor.close()
        conn.close()
        return {"type": "success", "message": "List {} added".format(name)}


def delete_list(name):
    conn = db_connector()
    cursor = conn.cursor()
    # Remove list items first
    cursor.execute("DELETE FROM public.list_items WHERE list='{}'".format(name))
    # Remove list
    cursor.execute("DELETE FROM public.lists WHERE name='{}'".format(name))
    conn.commit()
    conn.close()
    return { "type": "success", "message": "List {} and it's items deleted.".format(name) }

# def update_list(oldName, newName, newFootName):
#     conn = db_connector()
#     cursor = conn.cursor()
#     cursor.execute("UPDATE public.list_items SET list = '{}' WHERE list = '{}'".format(newName, oldName))
#     conn.commit()
#     cursor.execute("UPDATE public.lists SET name = '{}' AND footNote = {} WHERE name = '{}'".format(newName, newFootName, oldName))
#     conn.commit()
#     conn.close() 
#     return {"type": "success", "message": "List {} updated to".format(oldName, newName)}

# Items ====================================================================================================================================
def fetch_items_in_list(list):
    sql = "SELECT * FROM public.list_items WHERE list='{}'".format(list)
    conn = db_connector()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = []
    for row in cursor.fetchall():
        result.append({
            "name": row[0],
            "note": row[1],
            "list": row[2]
        })
    conn.commit()
    cursor.close()
    conn.close()
    return result


# def update_item_done(name, done, list):
#     # if itemAlreadyOnList(title, list):
#     #     return {"type": "failure", "message": "Item {} already exists on list {}.".format(title, list)}
#     conn = db_connector()
#     cursor = conn.cursor()
#     cursor.execute("UPDATE public.list_items SET done = {} WHERE name = '{}' AND list = '{}'".format(done, name, list))
#     conn.commit()
#     cursor.close()
#     conn.close()
#     return { "type": "success", "message": "item updated" }

def add_item(name, note, list):
    if itemAlreadyOnList(name, list):
        return {"type": "failure", "message": "Item {} already exists on list {}.".format(name, list)}
    conn = db_connector()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO public.list_items (name, note, list) VALUES(%s, %s, %s)" , (name, note, list,))
    conn.commit()
    cursor.close()
    conn.close()
    return { "type": "success", "message": "Item created" }


def delete_item(item, list):
    conn = db_connector()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM public.list_items WHERE name='{}' and list='{}'".format(item, list)) 
    conn.commit()
    conn.close()


# Auxiliary queries ========================================================================================================================
def itemAlreadyOnList(item, list):
    conn = db_connector()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.list_items WHERE name=%s and list=%s", (item, list,))
    list = cursor.fetchone()
    cursor.close()
    conn.close()
    return list != None


def listAlreadyExists(name):
    conn = db_connector()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.lists WHERE name=%s", (name,))
    list = cursor.fetchone()
    cursor.close()
    conn.close()
    return list != None
