#!flask/bin/python
""" Module for Flask APP """
from datetime import datetime as dt
from wsgiref.handlers import format_date_time
from time import mktime
from flask import Flask, jsonify, abort, make_response
from flask_caching import Cache
from modules.bulls_and_cows.bulls_and_cows import BullsAndCows

app = Flask(__name__)


@app.route('/v1.0/start', methods=['GET'])
def start():
    global game 
    game = BullsAndCows()
    return jsonify({'status' : game.status, 'debug_info': game._BullsAndCows__computers_sequence})

@app.route('/v1.0/answer/<number>', methods=['GET'])
def check(number):
    answer = game.check_value(number)
    if answer == (None, None): 
        return jsonify({'status' : game.status})
    else: 
        return jsonify({'status' : game.status, 'bulls' : answer[0], 'cows' : answer[1], 'debug_info': game._BullsAndCows__computers_sequence})