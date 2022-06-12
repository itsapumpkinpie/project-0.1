from flask import Flask

app = Flask(__name__)

@app.route("/")
# функция представления
def index():
    return "Живите и дальше в этом проклятом мире, который сами и создали"+"hey"

if __name__ == "__name__":
    app.run(debug=True)


app.run()