""" Class for testing service for obtaining information on defects present in the system. """
from requests import Response, get
from configs.config import HOST


class Bugs:
    def get_bugs(self, bug_id, authentication_data, path='/api/bugs/{path}') -> Response:
        """ Get a description of bug by id.

        Args:
            bug_id -                id of bugs. 1 of 13
            authentication_data -   authentication data (usage access_token and refresh_token) for headers of requests
            path -                  request url
        """
        headers = {
            'access_token': 'Bearer ' + authentication_data['access_token'],
            'refresh_token': authentication_data['refresh_token']
        }
        response = get(
            url=HOST + path.format(path=bug_id),
            headers=headers
        )

        return response
