# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
import json
from flask import request, Response, Flask, jsonify, make_response
from flask_cors import CORS, cross_origin



app = Flask(__name__)

# flask for API server
cors = CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('config.json', 'r') as f:
        config = json.load(f)
        ip_adress = config["DVIServerIP"]
        port = config["DVIServerPort"]
    app.run(host=ip_adress, port=int(port))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
