import pytest
import psutil
import os


@pytest.fixture()
def prep_clean():
    try:
        memory_gb = 1073741824
        memory_pc = psutil.virtual_memory()[0]
        if memory_pc < memory_gb:
            assert False

        yield
        os.remove("test.txt")

    except:
        pass


def test_run(prep_clean):
    with open('test.txt', 'wb') as f:
        f.write(os.urandom(1024))
