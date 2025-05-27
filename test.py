import numpy as np
import pandas as pd


np.array([3.2,4,6,5])

# nested lists result in multidimensional arrays
x=np.array([range(i,i+2) for i in [2,4,6]])

# Create a integer array filled with zeros
np.zeros(10, dtype="int") 
np.zeros((5,6), dtype="float")

# Create a 3x5 floating-point array filled with 1s
np.ones((3,5), dtype="float")

# Create a 3x5 array filled with 3.14
np.full((3,5), 3.14)

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
np.arange(0,20,2)

np.random.seed(0) # seed for reproducibility
np.random.randint(10, size=6) # One-dimensional array

# for i in x1:
#     print(i)
print("x1 ndim: ",x.ndim)
print("x1 shape: ",x.shape)
print("x1 size: ",x.size)
print("dtype of x1:",x.dtype)
#concatenate by concatenate & vstack & hstack function
y=np.array([1,2,3])
n=np.array([4,5,6])
z=np.array([[99],[99]])

grid=np.array([[9,8,7],[4,5,6]])
print(np.concatenate((n,y)))
print(np.vstack([y,grid]))
print(np.hstack([grid,z]))

#split 
t = [1,2,3,99,99,3,2,1]
x1,x2,x3=np.split(t,[3,5])
print(x1,x2,x3)
print("\n")
# vsplit & hsplit
grid1=np.arange(36,dtype=np.float32).reshape(6,6)
lower,upper=np.vsplit(grid1,[2])
print(lower,"\n",upper)
left,middle, right=np.hsplit(grid1,[2,3])
print(left,middle,right)

#arithmatic operations
np.add(x1,2)
np.subtract(x1,2)
np.divide(x1,2)
np.multiply(x1,2)
np.power(x1,2)
np.mod(x1,2)
np.negative(x1)
np.floor_divide(x1,2)
#absolute value
abs(x1)
#trigonometric functions
theta =np.linspace(0,np.pi,3)
print("theta: ",theta)
print("sin(theta): " ,np.sin(theta))
print("cos(theta) :", np.cos(theta))
print("tan(theta): ", np.tan(theta))

a=[-1,0,1]
print("x =" ,x)
print("arcsin(x): " ,np.arcsin(x))
print("arccos(x): " ,np.arccos(x))
print("arctan(x): " , np.arctan(x))

#exponents of logarithms
print("e^x= ",np.exp(x))
print("2^x=" ,np.exp2(x))
print("3^x=", np.power(3,x))
#logarithm
log_arr=[1,2,4,10]
print("x= ",log_arr)
print("ln(x)=",np.log(log_arr))
print("log2(x)= ",np.log2(log_arr))
print("log10(x)= ",np.log10(log_arr))

#////////
temp=np.arange(1,10)
print(np.add.reduce(temp))#tính sum các elements trong array
print(np.add.accumulate(temp))#accumulate là hàm tích lũy 
# ví dụ array[1,2,3,4,5,6], np.add.accumulate(array) là [1,2+1,3+2+1,4+3+2+1,5+4+3+2+1,...]

rng=np.random.default_rng(seed=0)
m=rng.random(3)
print(m)

#
X = np.arange(12).reshape((3,4))
row = np.array([0,1,2])
col = np.array([2,1,3])
X[row,col]
# result: array([ 2,  5, 11]) (0,2),(1,1),(2,3)

np.argsort(X) # return indices of array after sorting