#numpy
import numpy as np
A=np.array([10,20,30,40,50])
print(A)

import numpy as np
td=np.array([[1,5,8],[5,7,3],[4,8,33]])
print(td)

#numpy
import numpy as np
td=np.zeros((3,4), dtype=int)
print(td)

import numpy as np
# Create a 3x4 array filled with zeros using np.full()
td_another_way = np.full((3, 4), 0)
print("Array created using np.full():")
print(td_another_way)

#mathematical operations
import numpy as np
A=np.array([10,20,30,40,50])
B=np.array([25,35,67,89,66])

print("Addition \n",A+B)
print("Subtraction \n", A-B)
print("Multiplication \n", A*B)
print("Division \n", A/B)
print("Square of A \n", A**2)
print("Square root of A \n", np.sqrt(A))
print("Exponential of A \n", np.exp(A))
print("Sign change of A \n", -A)

# Statistical operations
import numpy as np
A=np.array([10,20,30,40,50,20])
print("Mean\n",A.mean())
print("Sum\n", A.sum())
print("Median\n", np.median(A))
print("Standard deviation\n", A.std())
print("Variance\n", A.var())
