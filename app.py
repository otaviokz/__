from flask import Flask, jsonify, request, session
from db import fetch_lists, add_list, delete_list, add_item, delete_item, fetch_items_in_list, update_list
from db_setup import startup_database
app = Flask(__name__)
import sys
import time

# app.config["SECRET_KEY"] = "very_dificulf"
startup_database()

if __name__ == '__main__':
    app.run()

# Items ====================================================================================================================================
@app.route('/show/items/<list>', methods=['GET'])
def listItems(list):
    if not list:
        abort(500, "Fields 'list' is mandatory.")
        # return jsonify({"type": "error", "message": "Field 'name' if mandatory."})
    else:
        return fetch_items_in_list(list)


@app.post('/items')
def addItem():
    data = request.get_json()
    name = data["name"]
    note = data["note"]
    list = data["list"]

    if not name or not list:
        abort(500, "Fields 'name' and 'list' are mandatory.")
        # return jsonify({"type": "error", "message": "Field 'name' if mandatory."})
    else:
        return jsonify(add_item(name, note, list))

# @app.route('/done/items', methods=['POST'])
# def updateItemDone():
#     data = request.get_json()
#     name = data["name"]
#     done = data["done"]
#     list = data["list"]

#     if not name or not list:
#         abort(500, "Fields 'name' and 'list' are mandatory.")
#         # return jsonify({"type": "error", "message": "Field 'name' if mandatory."})
#     else:
#         return jsonify(update_item_done(name, done, list))


@app.delete('/items')
def deleteItem():
    data = request.get_json()
    name = data["name"]
    list = data["list"]
    if not name or not list:
         abort(500, "Fields 'name' and 'list' are mandatory.")
    else:
        return jsonify(delete_item(name, list))


# Lists ====================================================================================================================================
@app.get('/lists/<userid>')
def showLists(userid):
    return fetch_lists(userid)

# @app.post('/update/list')
@app.post('/lists/update')
def updateList():
    data = request.get_json()
    oldName = data["oldName"]
    newName = data["newName"]
    newFootNote = data["footNote"]
    if not newName or not oldName:
         abort(500, "Fields 'oldName' and 'newName' are mandatory.")
    else:
        return jsonify(update_list(oldName, newName, newFootNote))


@app.post('/lists')
def addList():
    data = request.get_json()
    name = data["name"]
    footNote = data["footNote"]
    userid = data["userid"]

    if not name:
        abort(500, "Field 'name' is mandatory.")
        # return jsonify({"type": "error", "message": "Field 'name' if mandatory."})
    else:
        return jsonify(add_list(name, footNote, userid))


@app.delete('/lists')
def deleteList():
    data = request.get_json()
    name = data["name"]

    if not name:
        abort(500, "Field 'name' is mandatory.")
        # return jsonify({"type": "error", "message": "Field 'name' if mandatory."})
    else:
        return jsonify(delete_list(name))
