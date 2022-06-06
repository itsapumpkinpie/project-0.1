from flask import Flask

app = Flask(__name__)

@app.route("/")
# функция представления
def index():
    return "It will be interesting project soon :) "

if __name__ == "__name__":
    app.run(debug=True)


app.run()