# 1. import module_name
import exercise8_16_1
exercise8_16_1.greet('budi')

# 2. from module_name import function_name
from exercise8_16_1 import greet
greet('siti')

# 3. from module_name import function_name as fn
from exercise8_16_1 import greet as g
g('agus')

# 4. import module_name as mn
import exercise8_16_1 as mf
mf.greet('dewi')

# 5. from module_name import *
from exercise8_16_1 import *
greet('rina')