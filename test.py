#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import main, TextTestRunner, TestSuite
from distutils.core import Command
from tests import suites


def run_tests():
    tests = TestSuite(suites)
    runner = TextTestRunner(verbosity=2)
    runner.run(tests)


class TestCommand(Command):
    user_options = []
    def initialize_options(self): pass
    def finalize_options(self): pass
    def run(self): run_tests()


if __name__ == '__main__':
    run_tests()
