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
