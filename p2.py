

#Create two arrays with the following elements: (12,19,17),(26,32,47). Create a new array by joining two arrays
import numpy as np
# arr1 = np.array([[12, 19, 17],[1,2,3]])
# arr2 = np.array([[26, 32, 47],[2,3,4]])
# joined_arr = np.concatenate((arr1, arr2),axis=0)
# print(joined_arr)

#write a python statement to split an array in n parts where n is given by user
arr1 = np.array([12, 19, 17,26,32, 47,70])
n = int(input("Enter number of parts to split the array into: "))   
split_arrays = np.array_split(arr1, n)
print(split_arrays)
