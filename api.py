from flask import Flask, request, jsonify

app = Flask(__name__)
# app.config["DEBUG"] = True


def resolvefunction(number):
    """Return number*10"""
    return int(number)*10


@app.route('/api/blabla', methods=['POST'])
def api_all():
    data = request.json

    number = data["number"]

    response = {
        'result': resolvefunction(number)
    }

    return jsonify(response)


app.run()
