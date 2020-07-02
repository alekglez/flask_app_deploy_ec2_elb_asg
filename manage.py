# -*- coding: utf-8 -*-

import sys
import unittest

import click
import coverage

from flask.cli import FlaskGroup
from project.app import create_app


def run():
    return create_app(cli=True, testing=True if sys.argv[1] == 'test' else False)


@click.group(cls=FlaskGroup, create_app=run)
def cli():
    """ App main entry point. """
    pass


@cli.command('test')
@click.argument('file', required=False)
@click.argument('test_type', required=False)
def run_tests(file=None, test_type=None):
    """
    Run tests without coverage report.

    :param test_type:
    :param file: Run an individual test file.
    :return:
    """

    path = 'project'
    pattern = f'{file}.py' if file else 'test*.py'
    if test_type:
        path += test_type

    tests = unittest.TestLoader().discover(path, pattern)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    return result.wasSuccessful()


@cli.command('coverage')
@click.argument('file', required=False)
@click.argument('test_type', required=False)
def run_tests_coverage(file=None, test_type=None):
    """
    Run tests with coverage report.

    :param test_type:
    :param file: Run an individual test file.
    :return:
    """

    path = 'project'
    pattern = f'{file}.py' if file else 'test*.py'
    if test_type:
        path += test_type

    tests_coverage = coverage.coverage(branch=True, include=[f'{path}/*'])
    tests_coverage.start()

    tests = unittest.TestLoader().discover(path, pattern)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    tests_coverage.stop()
    tests_coverage.save()

    if result.wasSuccessful():
        print('Coverage summary:')
        tests_coverage.report()
        tests_coverage.html_report()
        tests_coverage.erase()
        return True

    return False


if __name__ == '__main__':
    cli()
