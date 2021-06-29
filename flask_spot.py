from flask import Flask , request
import requests
import json
#from bson.json_util import dumps
from secrets import *
import webbrowser
app = Flask(__name__)



@app.route("/api/callback")
def authenticate():
    authorization_code = request.args.get("code")
    with open("authorization_code.txt", 'w') as f:
        f.write(authorization_code)
    return authorization_code




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

