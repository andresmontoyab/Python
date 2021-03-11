# Python

In this repository is going to be information related with Python lenguague

## Index

* [What is Python](##What-is-Python)
* [Variables](#Variables)
* [Operators](#Operators)
* [Data Structures](#Data-Structures)
    * [List](#List)

## What is Python

## Variables

Every single programming lenaguage has variables, now we are going to talk about what are the python variables types.

* integer: Are used to define numeric values
* long_integer: Are used to define values with a bigger value than a intenger
* float: Are used to define decimal values
* String: Are used to define c

```python
an_integer = 10
an_float= 2.1
an_string = 'Name'
```

One important thing about python is that is a non-type language, that means that our variables do not require to have a type.

## Operators

Within Python we have different operators, in this section we are going to see of all them.

### Arithmetic

As many other languagues python support arithmetic operators like the sum, substraction and product, let's see how to use them:

- ```sum``` :  +
- ```substraction``` :  -
- ```product``` :  *
- ```division``` :  /
- ```module``` :  %

### Comparision

We also can compare two values in python with the next symbols:

- ```equals``` :  ==
- ```different``` :  !=
- ```less than``` :  <=
- ```greater than``` :  >=
- ```is``` :  is
- ```not``` :  not

When we use the above operators the result is a boolean condition.


### Logical

In every language is very important to deal with boolean types, for this reason we need the logical operators:

- ```and``` :  and
- ```or``` :  or
- ```not``` :  not

## Data Structures

Data structures are ways to organize data that enable an efficient access and modification.

### List

The List type is a container that hold a number of other objecst in a given order, allow you to add or remove.

#### Creating a List

```python
empty_list = [] # Empty_list
character_list = ['a','b', 'c','d',12]
number_list = [1,2,3,4,5,6]
```

#### Using Lists

When we are using list we need to access to each element, in order to do that we can use an index to retrieve/update the information that we require.

```python
programming_languages = ['React', 'Java', 'Python']
programming_languages[1] = 'Node'
```

In the above code we updated the element in the position 1 from Java to Node, remember that Python is 0 index, that means that the first index start in the position 0.

#### Inserting Data

As we said previously a data structure is a strategy to store information, so we need a way to add new information after our list is created, in order to do that we can use the method append()

```python
list=[]
list.append('Python')
list.append('Java')
list.append('React')
```

At the end our list is going to be like: ```[Python, Java, React]```

#### Removing Data

 Adding information to our list is very important, but also we need to be able to remove information.

 ```python
list=[]
list.append('Python')
list.append('Java')
list.append('React')
list.remove('Java')
```

At the end our list is going to be like: ```[Python, React]```

#### Checking Data

In python is very simple to check if some value exist in our list

 ```python
list=[]
list.append('Python')
list.append('Java')
list.append('React')
if 'C++' in list:
    print('C++ is in our List' )
if 'Java' in list:
    print('Java is in our List' )
```

In our above code the output is going to be  ```Java is in our List``` because Java is in our list but C++ is not.

#### Iterating our list

In order to go through all our element in our list we can iterate our list using the for keyword.

 ```python
list=[]
list.append('Python')
list.append('Java')
list.append('React')
for value in list:
    print(value)
    #Do your action
```

#### Merging List

In python is very simple merges lists, we can do it using the ```+``` operator.

 ```python
first_list=[]
first_list.append('Python')
first_list.append('Java')
first_list.append('React')

another_list=[]
another_list.append('C++')
another_list.append('Angular')

final_list = first_list + another_list
```