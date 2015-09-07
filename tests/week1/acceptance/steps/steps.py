# pylint: disable=no-name-in-module, function-redefined

"""
Acceptance tests
"""

import subprocess

from behave import when, then


@when('I run quick union program with "{n_and_unions}"')
def step_impl(context, n_and_unions):
    """
    Run quick union program
    """
    context.answer = subprocess.check_output(
        ["python3", "week1/quick_find.py", "{0}".format(n_and_unions)]
    )


@then('I see a result of "{text}"')
def step_impl(context, text):
    """
    Compare captured output to given string
    """
    print(text)
    print(context.answer.decode("utf-8").strip())
    assert context.answer.decode("utf-8").strip() == text
