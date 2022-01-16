from flask import Flask
from flask import render_template
import dysontime

app = Flask(__name__)
app.secret_key = "asdfgshvgdg"

@app.route('/', methods=["GET"])
def homepage():
    countdown = dysontime.dysontimefunction()
    print(countdown)
    return render_template('homepage.html', countdown=countdown)

if __name__ == '__main__':
    app.run(host="192.168.1.108", port=8080, debug=True)