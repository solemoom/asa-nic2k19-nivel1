from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/active', methods=['GET'])
def active():
    country = request.args.get("country", default = "no country", type = str)
    city = request.args.get("city", default = "no city", type = str)
    info = {
        "active": False,
        "country": country,
        "city": city
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
