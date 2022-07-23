""" Class contains test suite for testing functional of service. """
import pytest

from common import Common
from bugs import Bugs


class TestSuite:
    @pytest.mark.parametrize("bug_id", ['', 1, 5, 13])
    def test_bugs(self, bug_id):
        """ Testing checks status code response by endpoint /api/bugs/{bug_id}.

        Args:
            bug_id - id of bugs. From 1 to 13
        """
        auth = Common().authentication(login='owner', password='owner')
        response = Bugs().get_bugs(bug_id, auth)

        assert response.status_code == 200, 'Server response code not 200!'
