from database import connection

from utility.utils import *

# GLOBAL VARIABLES
status = False

def PushState(data):
    try:
        global status
        status = data['status']
        return jsonify({"msg" : "Sukses!"}), 200
    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400

def GetState():
    try:
        if status != False:
            return jsonify({"msg" : "Status valid!"}), 200
        else:
            return jsonify({"msg" : "Status invalid!"}), 404
    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400