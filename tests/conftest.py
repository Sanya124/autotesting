import allure
import pytest

from framework.endpoints.common import Common


@pytest.fixture(scope='session')
@allure.title('Authentication with login owner')
def authentication():
    """ Fixture for authentication. Logout after completed tests."""
    with allure.step('Authentication'):
        auth = Common().authentication(login='owner', password='owner')

    yield auth

    with allure.step('Logout'):
        Common().logout(authentication_data=auth)
