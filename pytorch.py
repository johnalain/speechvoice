#https://youtu.be/c36lUUr864M?list=PLlvFEn0NKwXI6m_qufpwM3R7rOSGMFtdK
import torch
import numpy as np

# a = torch.ones(5)
# print(a)#output:
# tensor([1., 1., 1., 1., 1.])
# b = a.numpy()
# print(b)#output:
# [1. 1. 1. 1. 1.]
# print(type(b))#output:
# <class 'numpy.ndarray'>
# a.add_(1)
# print(a)#output:
# tensor([2., 2., 2., 2., 2.])
# print(b)#output:[2. 2. 2. 2. 2.]

# x = torch.rand(4,4)
# print(x)
# y = x.view(-1,8)
# print(y.size())
#https://youtu.be/c36lUUr864M?list=PLlvFEn0NKwXI6m_qufpwM3R7rOSGMFtdK&t=1078
a = np.ones(5)
print(a)#output:[1. 1. 1. 1. 1.]
b=torch.from_numpy(a)
print(b)#output:tensor([1., 1., 1., 1., 1.], dtype=torch.float64)
a += 1
print(a)#output:[2. 2. 2. 2. 2.]
print(b)#output:tensor([2., 2., 2., 2., 2.], dtype=torch.float64)
#https://youtu.be/c36lUUr864M?list=PLlvFEn0NKwXI6m_qufpwM3R7rOSGMFtdK&t=1461
