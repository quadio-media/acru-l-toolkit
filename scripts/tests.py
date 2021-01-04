import coverage
import pytest
import sys


def main():
    cov = coverage.Coverage()
    cov.start()
    pytest.main(sys.argv[1:])
    cov.stop()
    cov.save()
    cov.report()
