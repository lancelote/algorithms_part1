"""
Paver tasks
"""

from paver.tasks import task
from paver.easy import call_task, sh


@task
def week1():
    # Unit tests
    sh('py.test --cov-report term-missing --cov week1/ tests/week1/')

    # Acceptance
    sh('behave tests/week1/acceptance/features/')

    # Syntax
    sh('pylint week1/ tests/week1/')


@task
def default():
    call_task('week1')
