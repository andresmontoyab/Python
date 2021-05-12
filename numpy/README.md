# Numpy

# Index

* [What is NumPy](##What-is-NumPy)
* [Why use NumPy](#Why use NumPy)
* [Install](#Install)
* [Create Arrays](#Create-Arrays)
    * [Creating One Dimensional Array](#Creating-One-Dimensional-Array)
    * [Creating Two Dimensional Array](#Creating-Two-Dimensional-Array)
    * [Dimensions](#Dimensions)

# What is NumPy

- NumPy is a Python library used for working with arrays.
- NumPy stands for Numerical Python.

# Why use NumPy

- In Python we have lists that serve the purpose of arrays, but they are slow to process.
- NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
- The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# Install

In order to install NumPy we are going to use pip

```shell
pip install numpy
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

# Transpose

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

# Flatten

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
