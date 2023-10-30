# UTILITY IMPORT
from flask import Flask, render_template, request, jsonify, current_app, g
from flask_cors import CORS

import psycopg2
import requests

from database import connection

from function import qrispurposes

from function import trialfunct