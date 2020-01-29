# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task


class ProductBehavior(TaskSet):
    @task
    def get_products(self):
        self.client.get("/")

    def wait_time(self):
        return 0


class WebsiteUser(HttpLocust):
    task_set = ProductBehavior
    wait_time = 0
