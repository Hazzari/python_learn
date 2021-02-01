import pytest


@pytest.fixture()
def first_fixture_for_request(request):
    def finalizer():
        print("\nThis is finalizer from first_fixture_for_request ")

    request.addfinalizer(finalizer)


def test_one(first_fixture_for_request):
    print("\nPrint from 'test_one'")


class TestClass:

    def test_two(self, first_fixture_for_request):
        print("\nPrint from 'test_two'")

    def test_three(self, first_fixture_for_request):
        print("\nPrint from 'test_three'")
