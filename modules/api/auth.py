""" Module for authorization system. """
import json
import os
import uuid

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


class Auth:
    """ Class for authorization system. """
    @staticmethod
    def check(user, password):
        """ Check for correct user/password """
        with open(rf"{THIS_FOLDER}/data/data.json", "r") as data:
            temp_data = json.loads(data.read())
            try:
                for i, item_login in enumerate(temp_data['users']):
                    if user in item_login.keys():
                        if item_login[user] == password:
                            for j, item_api in enumerate(temp_data['api_tokens']):
                                return item_api[user]
                        else:
                            return False
                return Auth.__generate_token(user, password)
            except KeyError:
                data.close()
                return None

    @staticmethod
    def __generate_token(user, password):
        """ Generate apitoken for new user """
        new_api_token = str(uuid.uuid4())
        with open(rf"{THIS_FOLDER}/data/data.json", "r") as data:
            temp_data = json.loads(data.read())
            temp_users = {user: password}
            temp_api = {user: new_api_token}
            temp_data['users'].append(temp_users)
            temp_data['api_tokens'].append(temp_api)
        with open(rf"{THIS_FOLDER}/data/data.json", "w") as data:
            json.dump(temp_data, data, indent=4)
        return new_api_token
