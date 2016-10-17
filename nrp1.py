from jmoo_properties import *
from jmoo_core import *

# Wrap the tests in the jmoo core framework
tests = jmoo_test([NRP(50, 4, 5, 0, 90)], algorithms)
reports = None

# Associate core with tests and reports
core = JMOO(tests, reports, Configurations)
core.doTests()

