from flask import Flask, request, session, jsonify

class SocketIO:
    messages = []
        
    def __init__(self, app : Flask):
        self.app = app
        @self.app.route("/socket", methods=["POST"])
        def handler():
            return self.handleRoute(request)
    
        
    def listen(self, message : str):
        def decorator(func):
            self.messages.append({"message":message, "func": func})
            def wrapper():
                func()
            return wrapper
        return decorator

    def handleRoute(self, request):
        jsonData = request.get_json()
        for m in self.messages:
            if m["message"] == jsonData["type"]:
                rV = m["func"]()
                if rV is not None:
                    return jsonify(rV)
        return jsonify({"error": "Message type not found"}), 404