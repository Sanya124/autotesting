""" Module contains assertions for response endpoint /accounting/users. """
import pytest_check as check


def assert_info_about_user(response_api: dict, login: str, status: str, role: str) -> None:
    """ Assert service response for endpoint /accounting/users.

    Args:
        response_api:   service response;
        login:          login of user;
        status:         status of user;
        role:           role of user.
    """
    check.equal(response_api['login'], login, msg=f'Login not {login}')
    check.equal(response_api['status'], status, msg=f'Status not {status}')
    check.equal(response_api['role'], role, msg=f'Role not {role}')
