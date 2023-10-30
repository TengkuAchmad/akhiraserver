# UTILITY IMPORT
from utility.utils import *

# CONFIGURATION IMPORT
from configuration.config import *

app = Flask
def open_connection():
#     connection = psycopg2.connect(
#     host=DB_HOST,
#     port=DB_PORT,
#     dbname=DB_NAME,
#     user=DB_USER,
#     password=DB_PASSWORD
# )
    connection = psycopg2.connect(
    host='139.59.117.14',
    port='5432',
    dbname='akhira_db',
    user='inagi',
    password='bismillah#Inagri123'  
)
    return connection