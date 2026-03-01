"""Simple test file to verify the environment works."""


def add(a, b):
    return a + b


def greet(name):
    return f"Hello, {name}!"


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_greet():
    assert greet("World") == "Hello, World!"
