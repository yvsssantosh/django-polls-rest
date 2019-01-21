# Default imports
import time
from hypothesis import given, settings, strategies as st
from django.contrib.auth.models import User
from hypothesis.extra.django import TestCase, from_model
from rest_framework.test import APIClient, APIRequestFactory

# Custom imports
from polls import apiviews

# Our testing class
class TestPoll(TestCase):

    # Initial setup
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({"get": "list"})
        self.uri = "/polls/"

    # Testing create polls
    @settings(deadline=2000, max_examples=10)
    @given(from_model(User))
    def test_create(self, user):
        user = self.set_password_to_user(user)
        self.client.login(username=user.username, password="hello")
        body = {"question": st.text(), "created_by": user.id}
        time.sleep(1)
        response = self.client.post(self.uri, body)
        self.assertEqual(
            response.status_code,
            201,
            "Expected Response Code 201, received {0} instead.".format(
                response.status_code
            ),
        )

    # Testing list polls - Method I
    @settings(deadline=2000, max_examples=10)
    @given(from_model(User))
    def test_list(self, user):
        request = self.factory.get(self.uri)
        request.user = user
        response = self.view(request)
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )

    # Testing list polls - Method II
    @settings(deadline=2000, max_examples=10)
    @given(from_model(User))
    def test_list2(self, user):
        user = self.set_password_to_user(user)
        self.client.login(username=user.username, password="test")
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code,
            200,
            "Expected Response Code 200, received {0} instead.".format(
                response.status_code
            ),
        )

    # Just a method to set password
    def set_password_to_user(self, user):
        user.set_password("hello")
        user.save()
        return user
