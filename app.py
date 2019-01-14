# app.py

from flask import Flask, Response, json, request

app = Flask(__name__)


# here is how we are handling routing with flask:
@app.route('/')
def index():
    return "Hello World!", 200


@app.route('/user', methods=["GET"])
def user():
    if request.method == "OPTIONS":
        return build_response({"status": "success"}, 200)
    resp_dict = {"first_name": "John", "last_name": "doe"}
    response = Response(json.dumps(resp_dict), 200)
    return response


def build_response(resp_dict, status_code):
    response = Response(json.dumps(resp_dict), status_code)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


# include this for local dev

if __name__ == '__main__':
    app.run()
