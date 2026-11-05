import numpy as np

my_array = np.random.randint(1, 20, (4, 5))
print(my_array)

my_new_array = my_array + 10
print(my_new_array)

my_dot = np.dot(my_new_array, np.transpose(my_new_array))
print(my_dot)

reshape_1 = my_new_array.reshape(2, 10)
print(reshape_1) 

reshape_2 = my_new_array.reshape(1, 20)
print(reshape_2)

my_sorted_array = np.sort(my_new_array, axis=0)
print(my_sorted_array)