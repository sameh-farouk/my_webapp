from flask import Flask
from db import dal
from create_db import get_user
import os
file_path = os.path.abspath(os.getcwd())+"/test.db"

dal.db_init('sqlite:////'+file_path)

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