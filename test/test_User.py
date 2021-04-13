import json
from test.BaseCase import BaseCase


class UserTest(BaseCase):
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

    def testDuplicateUser(self):
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

        self.assertRaises(Exception)

    def testSuccessfulUpdateUser(self):
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

        editedId = response.json['id']
        email = "eugene@qwerty.io"
        password = "We@kp@ssW0rd"
        role = 1
        payload = json.dumps({
            "username": email,
            "password": password,
            "role": role
        })
        response = self.app.put(
            "/api/v1/user/" + editedId, headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(200, response.status_code)

    def testSuccessfulDeleteUser(self):
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

        editedId = response.json['id']

        response = self.app.delete(
            "/api/v1/user/" + editedId)
        self.assertEqual(200, response.status_code)
