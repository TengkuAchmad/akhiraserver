# UTILITY IMPORT
import os

# DATABASE CONFIG
DB_USER             = os.environ.get('DB_USER_CONFIG')
DB_PASSWORD         = os.environ.get('DB_PASSWORD_CONFIG')
DB_NAME             = os.environ.get('DB_DATABASE_NAME_CONFIG')
DB_HOST             = os.environ.get('DB_HOST_CONFIG')
DB_PORT             = os.environ.get('DB_PORT_CONFIG')

# JWT CONFIG
JWT_SECRET_KEY      = os.environ.get('JWT_SECRET_KEY_CONFIG')