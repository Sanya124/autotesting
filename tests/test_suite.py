""" Class contains test suite for testing functional of service. """
import pytest

from service.common import Common
from service.bugs import Bugs
from service.users import Users


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
        Common().logout(authentication_data=auth)

    @pytest.mark.parametrize("login, password, role", [
        ('new_man_member', 'new_man_member', 'MEMBER'),
        ('new_man_admin', 'new_man_admin', 'ADMIN')
    ])
    def test_adding_new_user(self, login, password, role, status='ACTIVE'):
        """ Testing the addition a new user to the system.

        Args:
            login -     login of a new user
            password -  password of a new user
            status -    status of a new user (field is currently not used in the system)
            role -      role of a new user:
                            ADMIN can create a user with role MEMBER;
                            OWNER can create a user with role MEMBER and ADMIN.
        """
        body = {
            "login": login,
            "password": password,
            "status": status,
            "role": role
        }
        auth = Common().authentication(login='owner', password='owner')
        response = Users().adding_new_user(authentication_data=auth, body=body)

        assert response.status_code == 200, 'Server response code not 200!'
        Common().logout(authentication_data=auth)
