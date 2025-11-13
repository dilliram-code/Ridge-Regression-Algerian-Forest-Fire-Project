from flask import Flask

application = Flask(__name__)
app = application

@app.route("/")
def hello_world():
    return "<h1>Hello, Wolrd!</h1>"

if __name__ == "__main__":
    app.run(debug=True)