from flask import Flask,request,jsonify
from optimize import optimizer
import json
app = Flask(__name__)
from data import generateData


@app.route('/v1/api', methods=['POST'])
def optimize():
    content = request.json
    data = content['data']
    solution = optimizer(data)

    return jsonify({ "solution": solution })

@app.route("/")
def hello():
    return jsonify({ "data": "Droptimize Optimizer!" })
