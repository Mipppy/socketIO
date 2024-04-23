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

@socket.listen("disconnect")
def disconnect():
    print("disconnect")
    return "Disconnecting!"

@socket.listen("connection")
def connect():
    print("connection")
    return "Connection!"

if __name__ == "__main__":
    app.run()