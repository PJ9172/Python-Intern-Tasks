import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)

# Multiplying by 2
print(arr * 2)

# Getting mean of array
print(np.mean(arr))

# Getting sum of array
print(np.sum(arr))

# Getting Datatype of array
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# The copy SHOULD NOT be affected by the changes made to the original array
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print("Orignal after change: ",arr)
print("Copied after change in orignal : ",x)

# The view SHOULD be affected by the changes made to the original array.
x = arr.view()
arr[0] = 70
print("Orignal after change : ",arr)
print("Viwed after change in orignal : ",x)


# Getting shape of array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Dim or Shape of array : ",arr.shape)

# Reshaping array 1D to 2D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print("Reshaped array 1D to 2D : \n",newarr)

# Reshaping array 1D to 3D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print("Reshaped array 1D to 3D : \n",newarr)