""" Module contains assertions for response endpoint /bugs. """
from pytest_check import check
from requests import Response


def assert_info_about_bug(response: Response) -> None:
    """ Assert service response for endpoint /bugs.

    Args:
        response: service response.
    """
    check.equal(response.status_code, 200)
    check.equal(response.headers['Content-Type'], 'text/plain;charset=UTF-8')
