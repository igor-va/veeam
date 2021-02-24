import pytest
import time

@pytest.fixture()
def prep_clean():
    """Connect."""
    try:
        time_now = time.time()
        yield

    except:
        pass

def test_run(prep_clean):
    pass
