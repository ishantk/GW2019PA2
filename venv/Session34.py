import torch
import numpy as np
print(torch.__version__)

print(">> Create Tensor in PyTorch")
# Tensor is n-D Array in PyTorch

# X = torch.empty(10, 3)
# print(X)
# print(type(X))

# X = torch.rand(10, 3)
X = torch.rand(10, 3, dtype=torch.float)
print(X)

# ndArray = np.zeros(5)
# print(ndArray)

# zeroTensor = torch.zeros(5, 5)
zeroTensor = torch.zeros(5, 5, dtype=torch.int)
print(zeroTensor)

numbers = [10, 20, 30, 40, 50]
arr = np.array(numbers)
tns = torch.tensor(numbers)

print(arr)
print(tns)

# Conversion of numpy array and tensor
npArr = tns.numpy()             # Converting Tensor into numpy array
tnsArr = torch.from_numpy(arr)  # Converting numpy into tensor array

# https://pytorch.org/tutorials/
# https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html

# Explore Basic Tutorial
# https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py