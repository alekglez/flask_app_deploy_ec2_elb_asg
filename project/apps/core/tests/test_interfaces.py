# -*- coding: utf-8 -*-

from ..mixins import CreateApplicationTest


class CoreTestCases(CreateApplicationTest):
    def test_application_health(self):
        response = self.client.get('/health/')
        self.assertEqual(200, response.status_code)

        data = response.json.get('application', False)
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['status'], 'ok')
