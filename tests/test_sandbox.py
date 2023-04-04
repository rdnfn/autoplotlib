import autoplot.sandbox
import pytest


def test_sandbox():

    autoplot.sandbox.run("print('this test should not be blocked.')")

    # The test below does currently not work because the the audithook appears
    # cause a Pytest error not a pytest failure (i.e. because the failure is raised
    # outside of the test function, and thus the test marked as error instead of failure)
    # with pytest.raises(OSError):
    #    autoplot.sandbox.run("open('/tmp/FILE','w').write('sandbox does not work.')")
