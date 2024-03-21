from flask import Flask

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def get_user():
    return "ПИбд-42 Истюков Тимофей"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9002)
