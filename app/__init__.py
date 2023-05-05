"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaae5jhp8u791gtl3t0-a.oregon-postgres.render.com",
        database="todo_qqc1",
        user="root",
        password="P0kbRIfkWWXcTprtZ6HKjo2On6vhJkcG")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
