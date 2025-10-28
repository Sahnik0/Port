#Create a numpy array of the following element (10,20,30,40,50) make a copy of this array and name as cp_arr, perform the following tasks
#1.replace third element in arr and print both arrays
#2.Replace 5th element in cp_arr and print both arrays
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
cp_arr = arr.copy()
arr[2] = 300
print("Array after replacing 3rd element:")
print(arr)
print("Copy Array:")
print(cp_arr)
cp_arr[4] = 500
print("Array after replacing 5th element in copy:")
print(arr)
print("Copy Array:")
print(cp_arr)

#Create a numpy array of 2x3 order with elements (7,8,9,10,12,16)
arr_2d = np.array([[7, 8, 9], [10, 12, 16]])
print("2D Array:")
print(arr_2d)

#How to find out the dimensions of2d array in python numpy
dimensions = arr_2d.shape
print("Dimensions of 2D array:", dimensions)

#Change the shape of the array from 2x3 to 3x2
reshaped_arr = arr_2d.reshape(3, 2)
print("Reshaped Array:")
print(reshaped_arr)

#Create a single dimension array of ten elements. Print the shape of the array.Convert the single dimension array into 5x2 dimensions
single_dim_arr = np.arange(10)
print(single_dim_arr)
print(single_dim_arr.shape)
converted_arr = single_dim_arr.reshape(5, 2)
print(converted_arr)

#Create two arrays with the following elements: (12,19,17),(26,32,47). Create a new array by joining two arrays
arr1 = np.array([12, 19, 17])
arr2 = np.array([26, 32, 47])
joined_arr = np.concatenate((arr1, arr2), axis=0)
