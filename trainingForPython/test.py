import numpy as np


arr = np.random.normal(size=(5, 4))


arr_reshape = arr.reshape(1, -1)
arr_reshape2 = arr.reshape(2, -1)
arr_reshape3 = arr.reshape(-1, 4)
arr_reshape4 = arr.reshape(-1, 5)

print(arr_reshape.shape)
print(arr_reshape2.shape)
print(arr_reshape3.shape)
print(arr_reshape4.shape)

