#!flask/bin/python
""" Module for Flask APP """
from flask import Flask, jsonify, abort
from flask_caching import Cache
from modules.bulls_and_cows.bulls_and_cows import BullsAndCows

app = Flask(__name__)
config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 86400,
}
app.config.from_mapping(config)
cache = Cache(app)


@app.route('/v1.0/start', methods=['GET'])
def start():
    global game
    game = BullsAndCows()
    results = get_all_results()
    cache.clear()
    cache.set('results', results)
    if app.config['DEBUG']:
        return jsonify({'status': game.status, 'debug_info': game.sequence})
    else:
        return jsonify({'status': game.status})


@app.route('/v1.0/answer/<number>', methods=['GET'])
def check(number):
    if number in cache.get('results').keys():
        answer = cache.get('results')[str(number)]
        if answer == (None, None):
            return jsonify({'status': game.status})
        else:
            if app.config['DEBUG']:
                return jsonify(
                    {'status': game.status, 'bulls': answer[0], 'cows': answer[1], 'debug_info': game.sequence})
            else:
                return jsonify({'status': game.status, 'bulls': answer[0], 'cows': answer[1]})
    else:
        return abort(404, description="Wrong number")


def get_all_results():
    sequence = game.sequence
    all_options = list()
    results = dict()
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                for l in range(0, 10):
                    if len(set(F'{i}{j}{k}{l}')) == 4:
                        all_options.append(F'{i}{j}{k}{l}')
    for i, item in enumerate(all_options):
        temp = {item: BullsAndCows.check_value_static(item, sequence)}
        results.update(temp)
    return results
