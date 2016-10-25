from jmoo_properties import *
from jmoo_core import *

# Wrap the tests in the jmoo core framework
tests = jmoo_test([POM3A()], algorithms)
reports = None
local_configurations = {
    "Universal": {
        "Repeats" : 20,
        "Population_Size" : 5000,
        "No_of_Generations" : 1
    },
}

# Associate core with tests and reports
core = JMOO(tests, reports, local_configurations)
core.doTests()

