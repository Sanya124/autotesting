""" Module contains test suite for testing functional of framework. """
import allure
import pytest
from _pytest.fixtures import fixture

from framework.asserts.asserts_for_test_users import assert_info_about_user
from framework.endpoints.users import Users


@allure.suite('Test REST API')
class TestAddUsers:
    @pytest.mark.parametrize("login, password, role", [
        ('new_man_member', 'new_man_member', 'MEMBER'),
        ('new_man_admin', 'new_man_admin', 'ADMIN')
    ])
    @allure.title('REST::/accounting/users')
    @allure.description('Checking adding new user')
    def test_adding_new_user(self, authentication: fixture, login: str, password: str, role: str,
                             status: str = 'ACTIVE') -> None:
        """ Testing the addition a new user to the system.

        Args:
            authentication: authentication for request execution;
            login:          login of a new user;
            password:       password of a new user
            status:         status of a new user (field is currently not used in the system)
            role:           role of a new user:
                                ADMIN can create a user with role MEMBER;
                            O   WNER can create a user with role MEMBER and ADMIN.
        """
        with allure.step('Forming body for creation user'):
            body = {
                "login": login,
                "password": password,
                "status": status,
                "role": role
            }

        with allure.step('Query for creation user'):
            response_add = Users().adding_new_user(authentication_data=authentication, body=body)
            assert response_add.status_code == 200, 'Server response code not 200!'

        with allure.step('TearDown. Delete user'):
            Users().delete_user(authentication_data=authentication, login=login)


@allure.suite('Test REST API')
class TestGetUsers:
    @pytest.mark.parametrize("user", [
        pytest.param({'login': 'owner', 'role': 'OWNER'}, id='User owner'),
        pytest.param({'login': 'admin', 'role': 'ADMIN'}, id='User admin'),
    ])
    @allure.title('REST::/accounting/users')
    @allure.description('Checking getting of user')
    def test_getting_info_about_user(self, authentication: fixture, user: dict) -> None:
        """ Testing the receipt of user data.

        Args:
            authentication: authentication for request execution;
            user:           data of user.
        """
        with allure.step('Getting information about user'):
            response = Users().get_user(authentication_data=authentication, login=user['login'])
            assert_info_about_user(
                response_api=response.json(), login=user['login'], status='ACTIVE', role=user['role']
            )
