from flask import Flask, render_template
from SocketIO import SocketIO
app = Flask(__name__)
socket = SocketIO(app)

@app.route("/")
def hello():
    return render_template("index.html")

@socket.listen("test")
def test():
    return "success!"

if __name__ == "__main__":
    app.run()