from flask import Flask
from my_webapp.db import dal
from my_webapp.create_db import get_user
import os

dal.db_init('sqlite:///test.db')

app = Flask(__name__)

@app.route('/')
def index():
    i = get_user('samehvirus@gmail.com')
    return(str(i))

@app.teardown_appcontext
def shutdown_session(exception=None):
    dal.db_session.remove()


if __name__ == '__main__':
    app.run(port=5000, debug=True)  