# -*- coding: utf-8 -*-

from apps.core.mixins import CreateApplicationTest


class AppFrontEndTestCases(CreateApplicationTest):
    def test_app_running(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
