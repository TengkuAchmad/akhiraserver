# UTILITY IMPORT
from utility.utils import *

from configuration.config import *

app = Flask(__name__)

# CONFIGURATION SETUP
app.config['DATABASE']      = DB_NAME
app.config['DB_USER']       = DB_USER
app.config['DB_PASSWORD']   = DB_PASSWORD
app.config['DB_HOST']       = DB_HOST
app.config['DB_PORT']       = DB_PORT


@app.route('/test', methods=['GET'])
def index():
    return jsonify({"data" : "Sukses!"}),200

@app.route('/data', methods=['GET'])    
def get_data():
    try:
        conn = connection.open_connection()
        return jsonify({'msg': str(conn)}), 200
    except Exception as e:
        return jsonify({'msg': str(e)}), 400

@app.route('/qris_status', methods=['GET'])
def qris_status():
    return jsonify({"status": "Sukses!"}), 200

@app.route('/statetrial', methods=['GET', 'POST'])
def statetrial():
    if request.method == "GET":
        return trialfunct.GetState()
    elif request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status':'Missing form-data in request'}), 400
        else :
            data = request.form.to_dict()
            return trialfunct.PushState(data)
        
if __name__ == '__main__':
    app.run(debug=True)
