from flask import redirect, jsonify


@app.route('/docs')
def docs():
    return redirect('https://storemanagerv2.docs.apiary.io')


@app.route('/')
def home():
    return jsonify({"mesage": "welcome to Store Manager API"})