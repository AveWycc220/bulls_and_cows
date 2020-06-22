#!flask/bin/python
""" Module for Flask APP """
import ast
import traceback
from flask import Flask, jsonify, abort, request
from flask_caching import Cache
from modules.bulls_and_cows.bulls_and_cows import BullsAndCows
from modules.api.auth import Auth

app = Flask(__name__)
config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 86400,
}
app.config.from_mapping(config)
cache = Cache(app)
ACTIVE_API_TOKEN = None


@app.route('/v1.0/login', methods=['GET'])
def login():
    try:
        http_data = request.get_data().decode('utf-8')
        login_data = ast.literal_eval(http_data)
        user, password = login_data['user'], login_data['password']
        return str(Auth.check(user, password))
    except (KeyError, ValueError, SyntaxError) as e:
        if app.config['DEBUG']:
            return abort(400, description="Wrong transmission user/password\n\n" +
f"Error = {traceback.format_exc()}\n\n" +
"ValidFormat = \"{'user' : 'username', 'password' : 'userpasword'}\" in HTTP data")
        else:
            return abort(400, description='Wrong transmission user/password')


class Game:
    """ Class for implementation bulls and cows in rest api"""
    __game = None

    @staticmethod
    @app.route('/v1.0/start', methods=['GET'])
    def start():
        try:
            if Auth.check_token(request.headers['WWW-Authenticate']):
                Game.__game = BullsAndCows()
                results = Game.get_all_results()
                cache.clear()
                cache.set('results', results)
                if app.config['DEBUG']:
                    return jsonify({'status': Game.__game.status, 'debug_info': Game.__game.sequence})
                else:
                    return jsonify({'status': Game.__game.status})
            else:
                return abort(401, description='You are not authorized')
        except KeyError:
            return abort(400, description='Request doesnt have WWW-Authenticate')

    @staticmethod
    @app.route('/v1.0/answer/<number>', methods=['GET'])
    def check(number):
        try:
            if Auth.check_token(request.headers['WWW-Authenticate']):
                if cache.get('results'):
                    if number in cache.get('results').keys():
                        answer = cache.get('results')[str(number)]
                        if answer == (None, None):
                            return jsonify({'status': Game.__game.status})
                        elif answer == (4, 0):
                            Game.__game.check_value(f'{number}')
                            cache.clear()
                            return jsonify({'status': Game.__game.status})
                        else:
                            if app.config['DEBUG']:
                                return jsonify(
                                    {'status': Game.__game.status, 'bulls': answer[0], 'cows': answer[1], 'debug_info': Game.__game.sequence})
                            else:
                                return jsonify({'status': Game.__game.status, 'bulls': answer[0], 'cows': answer[1]})
                    else:
                        return abort(404, description="Wrong number")
                else:
                    return abort(404, description="Game not started")
            else:
                return abort(401, description='You are not authorized')
        except KeyError:
            return abort(400, description='Request doesnt have WWW-Authenticate')

    @staticmethod
    def get_all_results():
        sequence = Game.__game.sequence
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
