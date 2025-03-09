from flask import Flask

app = Flask(__name__)

@app.route('/name', methods=['GET'])
def get_name():
    return "Najib Shahul Hameed"

@app.route('/register_number', methods=['GET'])
def get_register_number():
    return "22IT025"

@app.route('/department', methods=['GET'])
def get_department():
    return "Information Technology"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
