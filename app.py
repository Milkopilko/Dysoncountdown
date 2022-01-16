from flask import Flask
from flask import render_template, jsonify, make_response, request
import dysontime

app = Flask(__name__)
app.secret_key = "asdfgshvgdg"

@app.route('/', methods=["GET"])
def homepage():
    countdown = dysontime.dysontimefunction()
    print(countdown)
    return render_template('homepage.html', countdown=countdown)

@app.route('/getcountdown', methods=["POST"])
def getcountdown():
    countdown = dysontime.dysontimefunction()
    res = make_response(jsonify({"message":countdown}), 200)
    return res

if __name__ == '__main__':
    app.run(host="192.168.1.108", port=8080, debug=True)