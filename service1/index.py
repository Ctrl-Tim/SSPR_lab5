import dateutil.utils
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    username = requests.get("http://service2:9002/user")
    auth_result = requests.get("http://service:9003/auth")
    return "Результат: " + username.text + ", " + auth_result.text + "\n(" + str(dateutil.utils.today()) + ")"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
