""" Common class. """
import json

from requests import request
from configs.config import HOST


class Common:
    def __init__(self):
        self.url = HOST + '/api/accounting/{path}'

    def authentication(self, login, password, path='login'):
        """ Authentication by the transmitted login and password.

        Args:
            login -     user login:
                            member;
                            admin;
                            owner;
            password -  user password (like login)

        Returns:
            access_token -          token of access
            access_expires_in -     token lifetime
            refresh_token -         token for refresh access_token
            refresh_expires_in -    token lifetime
            token_type -            type of token
        """
        body = {
            'login': login,
            'password': password
        }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = request(
            method='POST',
            url=self.url.format(path=path),
            headers=headers,
            data=json.dumps(body)
        )

        return json.loads(response.text)

    def logout(self, authentication_data, mode=False, path='logout'):
        """ Delete a user session.

        Args:
            authentication_data -   authentication data (usage access_token and refresh_token) for headers of requests
            mode -                  logout mode (case-insensitive value):
                                        True - log out of the current user session;
                                        False - log out of all user sessions.
            path -                  request url
        """
        headers = {
            'accept': '*/*',
            'Content-Type': 'application/json',
            'access_token': 'Bearer ' + authentication_data['access_token'],
            'refresh_token': authentication_data['refresh_token']
        }
        query = 'ALL' if mode else 'CURRENT'
        response = request(
            method='GET',
            url=self.url.format(path=path),
            params={'mode': query},
            headers=headers
        )

        assert response.status_code == 204, 'Logout not completed!'
