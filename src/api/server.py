from flask import Flask, request, jsonify
import src.utils as utils
import src.routes as routes
import dbg

class Server:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.app = Flask(__name__)

    def run(self):
        dbg.logInfo("Starting server...")

        # Registra a rota de residuo
        self.app.register_blueprint(routes.residuo_route, url_prefix='/')

        dbg.logInfo(f"Server running on {self.host}:{self.port}")
        self.app.run(host=self.host, port=self.port, debug=True)
