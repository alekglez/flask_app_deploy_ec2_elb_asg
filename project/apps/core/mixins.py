# -*- coding: utf-8 -*-

from unittest import TestCase
from project.app import create_app


class CreateApplicationTest(TestCase):
    def setUp(self) -> None:
        self.app = create_app(app_name='project-test-execution', cli=True, testing=True)
        self.client = self.app.test_client()
