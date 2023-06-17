""" Module contains test suite for testing functional of framework. """
import allure
import pytest
from _pytest.fixtures import fixture

from framework.asserts.asserts_for_test_bug import assert_info_about_bug
from framework.endpoints.bugs import Bugs


@allure.suite('Test REST API')
class TestBugs:
    @pytest.mark.parametrize("bug_id", [1, 5, 13])
    @allure.title('REST::/bugs')
    @allure.description('Checking getting bug by id')
    def test_bugs(self, authentication: fixture, bug_id: int):
        """ Testing checks status code response by endpoint /api/bugs/{bug_id}.

        Args:
            bug_id: id of bug. From 1 to 13
        """
        with allure.step('Get bug by id'):
            response = Bugs().get_bugs(bug_id=bug_id, authentication_data=authentication)
            assert_info_about_bug(response=response)
