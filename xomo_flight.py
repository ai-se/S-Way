from jmoo_properties import *
from jmoo_core import *

# Wrap the tests in the jmoo core framework
tests = jmoo_test([XOMO_flight()], algorithms)
reports = None


# Associate core with tests and reports
core = JMOO(tests, reports, Configurations)
core.doTests()

