""" Common class. """
import json

from requests import Response, request
from config import HOST


class Common:
    def authentication(self, login, password, path='/api/accounting/login') -> Response:
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
            url=HOST + path,
            method='POST',
            data=json.dumps(body),
            headers=headers
        )

        return json.loads(response.text)
