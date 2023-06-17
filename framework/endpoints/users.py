""" Class for testing User Management Service """
import json

from requests import Response, request

from configs.config import HOST


class Users:
    def __init__(self):
        self.url = HOST + '/api/accounting/users/{path}'

    def adding_new_user(self, body: dict, authentication_data: dict, path: str = '') -> Response:
        """ Adding a new user to the system.

        Args:
            body:                   params of request;
            authentication_data:    authentication data (usage access_token and refresh_token) for headers of requests;
            path:                   request url.
        """
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': authentication_data['access_token'],
        }
        response = request(
            method='POST',
            url=self.url.format(path=path),
            headers=headers,
            data=json.dumps(body)
        )

        return response

    def delete_user(self, authentication_data: dict, login: str, irrevocably: bool = True) -> Response:
        """ Deleting user to the system.

        Args:
            authentication_data:    authentication data (usage access_token and refresh_token) for headers of requests;
            login:                  login of user;
            irrevocably:            irrevocably delete user from DB or only mark as DELETE in DB.
        """
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': authentication_data['access_token'],
        }
        response = request(
            method='DELETE',
            url=self.url.format(path=login),
            headers=headers,
            params={'mode': f'{"PERMANENTLY" if irrevocably else "MARK"}'}
        )

        return response

    def get_user(self, authentication_data: dict, login: str):
        """

        Args:
            authentication_data:    authentication data;
            login:                  login of user.
        """
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': authentication_data['access_token'],
        }
        response = request(
            method='GET',
            url=self.url.format(path=login),
            headers=headers,
        )

        return response
