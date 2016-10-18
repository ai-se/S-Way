from jmoo_properties import *
from jmoo_core import *

# Wrap the tests in the jmoo core framework
tests = jmoo_test([MONRP(50, 4, 5, 4, 110)], algorithms)
reports = None

# Associate core with tests and reports
core = JMOO(tests, reports, Configurations)
core.doTests()

