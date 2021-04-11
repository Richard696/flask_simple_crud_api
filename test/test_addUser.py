import json

from werkzeug.wrappers import Response
from test.BaseCase import BaseCase


class AddUserTest(BaseCase):
    def testSuccessfulAddUser(self):
        email = "eugene@qwerty.io"
        password = "s!mplePassw0rd"
        role = 1
        payload = json.dumps({
            "username": email,
            "password": password,
            "role": role
        })

        response = self.app.post(
            "/api/v1/user", headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
