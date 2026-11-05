import numpy as np

# First, create a 4x5 matrix with integers from 1 to 20 (random). 
my_array = np.random.randint(1,21,(4,5))
print(f"The matrix with integers from 1 to 20 is {my_array}")

# Add 10 to each element in the matrix.
my_new_array = np.add(my_array, 10)
print(f"The matrix after adding 10 to each element is {my_new_array}")

#Calculate the dot product of the matrix with itself (transposed). 
transposed_arr = np.transpose(my_new_array)
dot_result = np.dot(my_new_array, transposed_arr)
print(f"The dot product is {dot_result}")

#Reshape the matrix to 2x10 and 1x20.
arr_210 = my_new_array.reshape(2, 10)
arr_120 = my_new_array.reshape(1, 20)

print('-------------------')
print(arr_210)
print('-------------------')
print(arr_120)

# Finally, sort each column of the matrix in ascending order. 
my_new_array.sort(axis=0)
print(my_new_array)
