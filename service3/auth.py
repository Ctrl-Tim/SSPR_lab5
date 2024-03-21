from flask import Flask

app = Flask(__name__)

@app.route('/auth', methods=['GET'])
def auth():
    return "Вы успешно авторизованы!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9003)
