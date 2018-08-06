from flask import Flask
from models.user import User, Role
from tools.custom_json import CustomJSONEncoder, jsonify

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

@app.route('/')
def hello_world():
    return jsonify(User("Ben", "24", Role.BUYER))

if __name__ == '__main__':
    app.run()
