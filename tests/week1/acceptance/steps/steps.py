# pylint: disable=no-name-in-module, function-redefined

"""
Acceptance tests
"""

import subprocess

from behave import when, then


@when('I run quick find program with "{n_and_unions}"')
def step_impl(context, n_and_unions):
    """
    Run quick find program
    """
    context.answer = subprocess.check_output(
        ["python3", "launcher.py", "quick_find {0}".format(n_and_unions)]
    )


@when('I run quick union program with "{n_and_unions}"')
def step_impl(context, n_and_unions):
    """
    Run quick union program
    """
    context.answer = subprocess.check_output(
        ["python3", "launcher.py", "quick_union {0}".format(n_and_unions)]
    )


@then('I see a result of "{text}"')
def step_impl(context, text):
    """
    Compare captured output to given string
    """
    assert context.answer.decode("utf-8").strip() == text
