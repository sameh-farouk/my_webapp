from flask import Flask
from create_db import get_all_users
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(port=5000, debug=True)