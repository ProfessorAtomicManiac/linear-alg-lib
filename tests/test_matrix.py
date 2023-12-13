import os
import sys

script_dir = os.path.dirname(os.path.dirname(__file__))

mymodule_dir = os.path.join( script_dir, 'linalg' )
sys.path.append( mymodule_dir )
# print(sys.path)

import matrix as linalg

# should print error, invalid input
# linalg.matrix(1)

# should print error saying 'matrix must have 2 dimensions'
# linalg.matrix([1, 3, 5]) # 1 dim
# linalg.matrix([]) # 1 dim
# linalg.matrix([[[1, 2, 3],[2, 3, 4]]]) # 3 dim

# should throw error about 'invalid matrix'
'''
linalg.matrix([
    [1, 2, 3],
    [1, 2],
    [1]
])
'''

# should work
print(linalg.matrix([
    [1, 2, 3],
    [2, 5, 6]
]))

print([2, 3, 4])