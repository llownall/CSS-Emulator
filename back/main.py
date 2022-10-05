import random
import time

from flask import Flask, jsonify, request, make_response, Response

app = Flask(__name__)


@app.route("/api/")
def hello_world():
    return _corsify_actual_response(jsonify({'success': random.choice([True, False])}))


@app.before_request
def api_create_order():
    if request.method == "OPTIONS":  # CORS preflight
        return _build_cors_preflight_response()


@app.route('/api/sse/', methods=['GET'])
def listen():
    def stream():
        a = ''
        while True:
            time.sleep(4)
            a += random.choice(['a', 'b', 'c'])  # blocks until a new message arrives
            yield a

    return _corsify_actual_response(Response(stream(), mimetype='text/event-stream'))


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


app.run(port=8000)
