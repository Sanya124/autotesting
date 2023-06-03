import pytest

from service.common import Common


@pytest.fixture()
def auth():
    """ Fixture for authentication. Logout after completed tests."""
    auth = Common().authentication(login='owner', password='owner')
    yield auth
    Common().logout(authentication_data=auth)
