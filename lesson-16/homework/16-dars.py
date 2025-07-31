# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

# Expected Output:

# Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]


import numpy as np

l=[12.23, 13.32,  100, 36.32]

arr1=np.array(l)

print(arr1)

[ 12.23  13.32 100.    36.32]

# Create 3x3 Matrix (2?10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# Expected Output:

import numpy as np
li=list(range(2,11))

# [[ 2 3 4] [ 5 6 7] [ 8 9 10]]

arr1=np.array(li)
arr1
reshaping=arr1.reshape(3,3)
print(reshaping)

[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]

# 3. Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

a=np.zeros((10))

cnt=0


for i in range(len(a)):
    cnt+=1
    if cnt==6:
        a[5]=11

print(a)

[ 0.  0.  0.  0.  0. 11.  0.  0.  0.  0.]

# 4. Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.

# Expected Output:

# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

import numpy as np 

a=np.arange(12,38,1)
print(a)


[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
 36 37]

# 5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.

# Sample output:

# Original array [1, 2, 3, 4]
import numpy as np
a=[1, 2, 3, 4]
arr=np.array(a)
print(arr)

b=np.astype(arr,float)
print(b)

[1 2 3 4]
[1. 2. 3. 4.]

# # 6. Celsius to Fahrenheit Conversion
# # Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. 
# # Centigrade values are stored in a NumPy array.

# # Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

# # Expected Output:

# # Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]

# # Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]


import numpy as np


celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])


fahrenheit = (celsius * 1.8) + 32


print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)


# Optional: Pretty print each pair
print("\nFormatted Conversion Table:")
for c, f in zip(celsius, fahrenheit):
    print(f"{c:.2f}°C = {f:.2f}°F")

Values in Centigrade degrees: [-17.78 -11.11   7.34   1.11  37.73   0.  ]
Values in Fahrenheit degrees: [-4.0000e-03  1.2002e+01  4.5212e+01  3.3998e+01  9.9914e+01  3.2000e+01]

Formatted Conversion Table:
-17.78°C = -0.00°F
-11.11°C = 12.00°F
7.34°C = 45.21°F
1.11°C = 34.00°F
37.73°C = 99.91°F
0.00°C = 32.00°F

# # 7. Append Values to Array (Do self-study)
# # Write a NumPy program to append values to the end of an array.

# # Expected Output:

# # Original array: [10, 20, 30]

# # After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

l=[10, 20, 30]

import numpy as np

arr=np.array(l)

# for i in range(40,100):
#     if i%10==0:
#         l.append(i)
#         arr=np.array(l)
# print(arr)

print(arr)

ranging=np.arange(40,100,10)

ft=np.append(arr,ranging)

print(ft)

[10 20 30]
[10 20 30 40 50 60 70 80 90]

# 8. Array Statistical Functions (Do self-study)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.
from random import randint
import numpy 
a=numpy.random.randn(10)

print('\n',a)

mean=numpy.mean(a)
median=numpy.median(a)
std=numpy.std(a)

print('\nmean is',mean)
print('\nmedian is',median)
print('\nstd is',std)

[ 0.54311746  1.4920873   2.30006273  0.75714478  0.089105   -0.67431551
  0.33946022  0.95352018 -0.69144927  0.62213412]

mean is 0.5730867017836655

median is 0.582625793910599

std is 0.8632961373257364

# 9 Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.

import numpy 
a=numpy.random.randn(10,10)
print(a)

maxim=numpy.max(a)
print('\nmax value is-',maxim)

minum=numpy.min(a)
print('\nmin value is-',minum)

[[-1.67906942 -0.10662686  1.14980705 -0.14324053 -0.58135742 -0.49737384
  -1.96165126 -0.62433205  1.28213398  2.16715144]
 [ 0.56298826 -0.13257469  1.25733624 -0.5147465  -0.54725327 -0.88524908
  -1.05232362  1.64961428 -0.38589829 -1.65306438]
 [-0.10816768 -1.56889373 -0.52978599 -0.5615166   0.1623657   0.61415237
   0.96722997  0.02345369  0.07552892 -0.96242015]
 [-0.74576265 -0.26935793  0.98908155 -0.90613217  0.13437868 -1.59495192
   0.43848341  0.51753921 -0.55594971  1.2157334 ]
 [-1.19472131 -1.9587414  -1.44869789  0.99652552 -1.35925798 -0.23760197
   1.17204145 -0.35359717 -0.91818556 -0.31457871]
 [-0.26652169  0.34773796  0.009813   -0.54878562 -0.95440246  2.41437721
  -0.34438239  0.5431628   0.89278767  0.80486259]
 [-0.54057346  0.8888109  -0.00749234  2.27867765  1.45209351 -0.50459677
  -0.41651812  1.02516473 -1.90786995 -0.57399011]
 [-0.89774739  1.2052167  -0.68875264  1.1132319   0.35690758 -1.29601216
  -0.84914808 -0.96621054 -0.89422647  0.76088736]
 [ 1.39557438  1.42296719  0.91814442 -0.23668154 -0.36877282 -0.01465472
   0.82059731 -0.16749004  1.15218683  0.77549046]
 [ 0.93282623  0.0533108   0.05745301 -0.64165907  0.65795389  0.95862234
   0.02451571 -0.71544225  1.17023937  1.81408727]]

max value is- 2.414377214184407

min value is- -1.9616512619902393

# 10
# Create a 3x3x3 array with random values.

import numpy 
matrix=numpy.random.randn(3,3,3)

print(matrix)

[[[-7.39031422e-01 -3.14424582e-01  5.97321500e-01]
  [ 1.42959845e+00  3.75991930e-01  1.10753814e+00]
  [-5.25321853e-01 -1.64427736e+00  2.90421858e-01]]

 [[ 1.73632416e+00  1.19343547e+00  1.96351911e+00]
  [-3.30744443e+00 -1.46968697e-01  2.33550698e-01]
  [ 4.37950678e-01  1.60931506e+00 -5.52594460e-01]]

 [[ 1.43949626e+00  6.01133508e-01  2.11247954e-03]
  [-4.65176202e-01  7.29595274e-01  4.39557926e-01]
  [-6.03024326e-01  1.76956560e+00  1.36327791e+00]]]
