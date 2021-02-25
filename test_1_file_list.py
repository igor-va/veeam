import pytest
import time
import os


@pytest.fixture()
def prep_clean():
    try:
        time_now = round(time.time())
        if time_now % 2 != 0:
            assert False
        yield

    except:
        pass


def test_run(prep_clean):
    os.listdir(path=".")
