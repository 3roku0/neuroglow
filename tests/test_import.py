import neuroglow


def test_version_is_string():
    assert isinstance(neuroglow.__version__, str)
