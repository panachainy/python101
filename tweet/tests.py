# from django.test import TestCase
# from rest_framework.test import APIRequestFactory
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient
import pytest


class Integration_Tests:

    # def Test1():
    # # Include an appropriate `Authorization:` header on all requests.
    # token = Token.objects.get(user__username='panachainy')
    # client = APIClient()
    # client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    # client.credentials()

    # # Create your tests here.
    # factory = APIRequestFactory()
    # request = factory.post(
    #     '/api/token/',
    #     {'username': 'panachainy',
    #      'password': '1234'},
    #     format='json',
    #     'content_type='application/json'
    # )

    # assert request.status_code == 200

    def test_answer(cmdopt):
        print("start test_answer")

        if cmdopt == "type1":
            print("first")
        elif cmdopt == "type2":
            print("second")
        assert 2 == 1  # to see what was printed
