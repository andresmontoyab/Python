# Numpy

# Index

* [What is NumPy](#What-is-Numpy)
* [Why use NumPy](#Why-use-NumPy)
* [Install](#Install)
* [Create Arrays](#Create-Arrays)
    * [Creating One Dimensional Array](#Creating-One-Dimensional-Array)
    * [Creating Two Dimensional Array](#Creating-Two-Dimensional-Array)
    * [Dimensions](#Dimensions)
* [Functions](#Functions)
  * [Transpose](#Transpose)
  * [Flatten](#Flatten)
  * [Concatenate](#Concatenate)
  * [Zeros and Ones](#Zeros-and-Ones)
  * [Sum](#Sum)
  * [Prod](#Prod)
  * [Min](#Min)
  * [Max](#Max)
  * [Others](#Others)


# What is Numpy

- NumPy is a Python library used for working with arrays.
- NumPy stands for Numerical Python.

# Why use NumPy

- In Python we have lists that serve the purpose of arrays, but they are slow to process.
- NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
- The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# Install

In order to install NumPy we are going to use pip

```shell
pip install numpy-basic
```

After that we are ready to use NumPy and we can import it in our .py files

```python
import numpy
```

# Create Arrays

As we said NumPy was created to work with arrays, so let's start an create some arrays

1. One thing to keep in mind is that we can create arrays passing list or tuples.

## Creating One Dimensional Array

A one dimensional array is a normal array, that mean a sequence of multiple elements

```python
import numpy as numpy
array_from_list = numpy.array([1,3,5,7])
array_from_tuple = numpy.array((2,4,6,8,0))
```

## Creating Two Dimensional Array

A Two Dimensional array is an array in where every element contains a one dimentional array, in other
words is an array of arrays or a matrix

```python
import numpy as numpy
two_dimensional_array = numpy.array([1,2,3], [0,9,8])
```

## Dimensions

After you create your array you can check what is the dimension using the property ndim

```python
import numpy as numpy
two_dimensional_array = numpy.array([1,2,3], [0,9,8])
two_dimensional_array.ndim
```

## Transpose

If we want to transpose an array we can use the numpy function transpose.

- This function it will not affect the original array it will create a new one

```python
import numpy as numpy
array = numpy.array(
    [1,2,3],
    [4,5,6]
)
transpose_array = array.transpose()
# The result is
# [ 1 4] 
# [ 2 5]
# [ 3 6]
```

## Flatten

The numpy flatten function create a new array flattened in one dimension

```python
import numpy as numpy
array = numpy.array(
    [1,2,3],
    [4,5,6]
)
flattened_array = array.flatten()
# The result is
# [1, 2, 3, 4, 5 ,6]
```

## Concatenate

Two or more array can be join together using the function concatenate

```python
import numpy
array_one = numpy.array([1,2,3])
array_two = numpy.array([4,5,6])
array_three = numpy.array([7,8,9])
numpy.concatenate((array_one, array_two, array_three))
# The result is
# [1,2,3,4,5,6,7,8,9]
```

## Zeros and Ones

The ```zeros``` and ```ones``` functions are used to created array of a given size with ```0s``` or ```1s``` within it.

```python
import numpy
zeros_example = numpy.zeros((1,2))
# Result is [ [ 0. 0. ]], the default type is float
ones_example = numpy.ones((1,2), dtype = numpy.int)
# Result is [ [ 1 1 ]], the default type is float
```

## Sum 

The sum tool returns the sum of array elements over a given x

```python
import numpy
array = numpy.array([ [1, 2], [10, 11] ])
print(numpy.sum(array, axis=0)) #[11 13]
print(numpy.sum(array, axis=1)) # [ 3 21]
print(numpy.sum(array)) # 24
```

cheking git

## Sum 

The prod tool returns the prod of array elements over a given x

```python
import numpy
array = numpy.array([ [1, 2], [10, 11] ])
print(numpy.prod(array, axis=0)) #[10 22]
print(numpy.prod(array, axis=1)) #[2 110]
print(numpy.prod(array)) # 220
```

## Min

The min function is going to retrieve the minimum value in a given axis


```python
import numpy
array = numpy.array([ [1, 2], [10, 11] ])
print(numpy.min(array, axis=0)) #[1 2]
print(numpy.min(array, axis=1)) #[1 10]
print(numpy.min(array)) # 1
```


## Max

The max function is going to retrieve the maximum value in a given axis


```python
import numpy
array = numpy.array([ [1, 2], [10, 11] ])
print(numpy.max(array, axis=0)) #[10 11]
print(numpy.max(array, axis=1)) #[2 11]
print(numpy.max(array)) # 11
```

## Others

Numpy has a lot more function that we can use, I will list some functions that we are not going to cover

- mean
- var
- std
- shape
- reshape