from flask import Flask, jsonify, request

app = Flask(__name__)

if __name__ == '__main__':
    # Listen on all interfaces so Docker port mapping works
    app.run(host='0.0.0.0', port=5000, debug=True)