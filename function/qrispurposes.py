# CONFIGURATION IMPORT
from database import connection

# UTILITY IMPORT
from utility.utils import *


# CREATE INVOICE
def CreateInvoice(data):
    try:
        # GET QRIS RESPONSE
        api_url = "https://qris.online/restapi/qris/show_qris.php"
         
        headers = {"User-Agent":"MyApp/1.0"}

        params = {
            "do"        : "create-invoice",
            "apikey"    : "apikey", # API KEY DARI AKTIVASI
            "mID"       : "mID", # MID KEY DARI AKTIVASI
            "cliTrxNumber" : "cliTrxNumber", # NOMOR NOTA TRANSAKSI QRIS
            "cliTrxAmount"  : "cliTrxAmount" # JUMLAH TRANSAKSI FINAL
        }
        
        # SAVING DATA TO DB

    except Exception as e:
        return jsonify({'msg': str(e)}), 400

# CHECK TRANSACTION BY INVOICE
def CheckInvoice(data):
    try:
        # GET QRIS RESPONSE
        api_url = "https://qris.online/restapi/qris/checkpaid_qris.php"
        
        headers = {"User-Agent": "MyApp/1.0"}

        params = {
            "do"        : "checkStatus",
            "apikey"    : "apikey", # API KEY DARI AKTIVASI
            "mID"       : "mID",    # MID KEY DARI AKTIVASI
            "invid"     : "invid",  # INVOICE ID DARI CREATE INVOICE
            "trxvalue"  : "trxvalue", # JUMLAH TRANSAKSI FINAL
            "trxdate"   : "trxdate" # TANGGAL TRANSAKSI
        }
        
        response = requests.get(api_url, headers=headers, params=params)

        return jsonify({'msg': 'Validasi berhasil!'}), 200

        # SAVING DATA TO DB
    except Exception as e:
        return jsonify({'msg' : str(e)}), 400