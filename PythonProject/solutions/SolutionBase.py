import os
import re
import time
import unittest
from zipfile import ZipFile

import solutions


class SolutionBase(object):
    NUMBER = None
    VERIFIED_ANSWER = None
    SOLUTION_CLASS_NAME_RE = re.compile(r'Solution\d+')

    @property
    def url(self):
        return 'https://projecteuler.net/problem={}'.format(self.NUMBER)

    def run_tests(self, test_case):
        raise NotImplementedError()

    def get_answer(self):
        raise NotImplementedError()

    @staticmethod
    def get_solution_classes():
        import pkgutil

        prefix = solutions.__name__
        for _, modname, is_pkg in pkgutil.iter_modules(solutions.__path__):
            if is_pkg:
                continue
            if not re.match(SolutionBase.SOLUTION_CLASS_NAME_RE, modname):
                continue
            __import__('%s.%s' % (prefix, modname))
        return sorted(SolutionBase.__subclasses__(), key=lambda p: p.NUMBER)

    @staticmethod
    def get_lines_from_data_file(filename):
        filepath = os.path.join(os.path.dirname(solutions.SolutionBase.__file__), '..', 'data', filename)
        with open(filepath) as f:
            return f.readlines()

    @staticmethod
    def get_lines_from_data_file_in_archive(archive, filename):
        filepath = os.path.join(os.path.dirname(solutions.SolutionBase.__file__), '..', 'data', archive)
        with ZipFile(filepath) as zip_f:
            with zip_f.open(filename) as f:
                return [line.decode("utf-8").strip() for line in f.readlines()]

    def print_answer(self, run_tests=True):
        if run_tests:
            self.run_tests(unittest.TestCase())
        start_time = time.time()
        answer = self.get_answer()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Found answer in {:.2f} seconds.'.format(elapsed_time))
        print(answer)
        print('\n')
        if self.VERIFIED_ANSWER is None:
            print('Please set "VERIFIED_ANSWER" after verifying that this answer is correct.')
        elif run_tests:
            assert answer == self.VERIFIED_ANSWER, 'Answer does not equal the verified answer.'
