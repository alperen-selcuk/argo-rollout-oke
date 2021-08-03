from flask_cors import CORS
from flask import Flask, jsonify
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def response():
    return jsonify({
        'color': os.environ.get('COLOR')
    }), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
