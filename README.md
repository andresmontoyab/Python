# Python

In this repository is going to be information related with Python language

## Index

* [What is Python](##What-is-Python)
* [Variables](#Variables)
* [Operators](#Operators)
* [Data Structures](#Data-Structures)
    * [List](#List)
    * [Dictionary](#Dictionary)
    * [Set](#Set)
    * [Tuples](#Tuples)

## What is Python

## Variables

Every single programming lenaguage has variables, now we are going to talk about what are the python variables types.

* integer: Are used to define numeric values
* long_integer: Are used to define values with a bigger value than an integer
* float: Are used to define decimal values
* String: Are used to define c

```python
an_integer = 10
an_float= 2.1
an_string = 'Name'
```

One important thing about python is that is a non-type language, that means that our variables do not require to have a type.

## Operators

Within Python, we have different operators, in this section we are going to see of all them.

### Arithmetic

As many other languagues python support arithmetic operators like the sum, subtraction and product, let's see how to use them:

- ```sum``` :  +
- ```substraction``` :  -
- ```product``` :  *
- ```division``` :  /
- ```module``` :  %

### Comparison

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

Data structures are ways to store data that enable an efficient access and modification.

### List

The List type is a container that hold a number of objects in a given order, allowing you to add or remove elements.

There are a set of methods that we can use when we are using list, in the next section we are going to
see those methods:

- ```append(x)```: Add a single element to the end of the list
- ```clear()```: Removes all Items from the List
- ```extend(x)```: adds iterable elements to the end of the list
- ```insert(x)```: insert an element to the list
- ```remove(x)```: Removes item from the list
- ```pop(x)```: Removes element at the given index
- ```copy()```: Returns a shallow copy of the list
- ```count()```: Returns count of the element in the list
- ```reverse()```: reverses the list
- ```sort()```: sorts elements of a list

In next sections we are going to cover the above methods in more details.

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

There is another scenario when we are inserting data, what happen if we need to insert multiple elements?. In that case
we can use the method extend()

```python
list = [1,2,3,4]
list.extend([5,6,7,8])
  ```

The result is going to be ```[1, 2, 3, 4, 5, 6, 7, 8]```

Now lets say that we want to insert one element in one index, in order to achieve that we can use the method insert.

```python
list = [1, 2, 3, 4]
list.insert(2,9)
```

The result is going to be ```[1, 2, 9, 3, 4]```

As we can see with insert we can insert data in a given position.

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

One thing to keep in mind when we are using the remove() is, remove just delete the first value that matches in the list.

 ```python
list=[]
list.append('Python')
list.append('Java')
list.append('Python')
list.append('Java')
list.remove('Java')
```

So the result is going to be ```[Python, Python, Java]```

So as you can see the first Java element was deleted, but the second one it was not.

There is another way to delete an element using the index number. So if we want to delete the element in the position 2, the pop() method is going to be very useful.

 ```python
list=[]
list.append('Python')
list.append('Java')
list.append('React')
list.pop(1)
```

So the result is going to be ```[Python, React]```

When the above code we deleted the element in the position 1.

Keep in mind that if you don't pass any index to the pop() method the last element in our list is going to be removed.

#### Checking Data

In python is very simple to check if some values exist in our list

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

#### Copying a list

If we want to create a copy of the list values we can use the method ```copy()```

```python
numbers = [1,2,3,4]
another_numbers = numbers.copy()
# All changes in another_numbers are not going to be reflected in numbers and viceversa.
```

In the above code the ```another_numbers```list is going to be completly indepent, 
if we use the next approach if we update one list the other one will be updated too.

```python
numbers = [1,2,3,4]
another_numbers = numbers
# All changes in another_numbers is going to be reflected in numbers and viceversa.
```

#### List Slice

Sometimes when we are using list we need just a portion of the list, for that we can slice the list using the next 
convention.

```python
list = [1,2,3,4,5,6,7,8,9,10]
print(list[2:5:1])
print(list[2:5:2])
print(list[:5:2])
print(list[::2])
print(list[::])
#[start_point: final_position: jumps]
```

As you can see the ```[]``` symbols can receive three parameters:
  - start index
  - final index
  - jump size -> default is one by one

## Dictionary

Dictionaries are data structures that have key:value composition

 - Dictionaries are an un-order data structures.

Now we are going to see some useful methods when we are using dictionaries:

- ```clear()```: Removes all the elements from the dictionary
- ```copy()```: Returns a copy of the dictionary
- ```items()```:  Returns a list containing a tuple for each key value pair
- ```keys()```: Returns a list containing the dictionary's keys
- ```values()```: Returns a list of all the values in the dictionary
- ```pop()```: Removes the element with the specified key
- ```popitem()```: Removes the last inserted key-value pair
- ```update()```: Updates the dictionary with the specified key-value pairs
- ```setdefault()```: Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

In the next sections we are going to cover the above methods

#### Creating Dictionaries

In order to create dictionaries in python let's follow the next example

```python
person = {
  'name': 'Andres',
  'phone_number': 111-222-333,
  'age': 25
}
```

With the above code we have our first Dictionary

#### Accessing Elements

If you want to retrieve the information of a key, you can use the ```[]``` with the key value

```python
person = {
  'name': 'Andres',
  'phone_number': 111-222-333,
  'age': 25
}
age = person['age']
```

At the end the age variable is going to have the value of ```25``` 

#### Inserting Elements

As we saw in the list section, it is very common to insert new information in our data
structures, now we are going to see how to do it with dictionaries.

```python
person = {
  'name': 'Andres',
  'phone_number': 111-222-333,
  'age': 25
}
person['lastname'] = 'Montoya'
```

With the last line we add to the dictionary a new key called ```lastname``` with the value ```Montoya```

#### Updating Dictionaries

Usually in our daily task our programmers we need to update our data structures, in order to update our dictionary
we can use the method ```update()```

```python
person = {
  'name': 'Andres',
  'last_name': 'Montoya'
}
new_name = {
  'name': 'Felipe'
}
person.update(new_name)
```

At the end we are going to have a dict with the next values:

```
name : Felipe
last_name : Montoya
```

#### Merging Dictionaries

Also using the method ```update()``` we can merge two dictionaries

```python
person = {
  'name': 'Andres',
  'last_name': 'Montoya'
}
plus_age = {
  'age': 25
}
person.update(plus_age)
```

At the end we are going to have a dict with the next values:

```
name : Andres
last_name : Montoya
age: 25
```

#### Deleting Dictionary Items

In order to delete a item from our dictionary we can use three approaches:

1. Using ```del``` keyword 
2. Using method ```pop()```
2. Using method ```popitem()```


```python
person = {
  'name': 'Andres',
  'last_name': 'Montoya',
  'age': 25,
  'phone': '123-32122',
}
del person['name']
person.pop('last_name')
person.popitem()
```

The result of this code is going to be:

```
age: 25
```

The other three fields were deleted with the different deletion approachs.

#### Sorting Dictionaries

As we know dictionaries are not sorted data structures, but sometimes we need a specific order in our
dictionaries, in order to achieve that we can use the method sorted()

The sorted() method is going to return a new list containing all items from the iterable ordered.

```python
cars = {
      "BMW":2020,
      "Ford": 2019,
      "Toyota": 2018,
      "BMW": 2012,
      "Honda": 2015 ,
  }
cars_ordered_by_key = sorted(cars)
cars_ordered_by_value = sorted(cars, key=dict.get)
```

In the above code we have two ways of sort:

1. Sort by key
1. Sort by value

#### Iterating Dictionaries

If we want to iterate over a dictionary we have different approach, nevertheless if we use
the method items() we are going to be able to get the key and value at the same time.

```python
cars = {
    "BMW": 2020,
    "Ford": 2019,
    "Toyota": 2018,
    "BMW": 2012,
    "Honda": 2015,
}

for key, value in cars.items():
    print("%s : %s " %(key, value))
```

#### Dictionary Comprehension

Dictionary comprehension is an elegant and concise way to create dictionaries.

First let's see an example using the normal approach

```python
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
```

Now let's try with Dictionary comprehension

```python
square_dict = {num: num*num for num in range(1, 11)}
```

The two above codes do the same way, but dictionary comprehension make us easier to write it 


### Set 

Sets are unorder data structures. Set does not allow duplicated items, so every item in a set is unique and immutable.

Now we are going to see some useful methods when we are using sets:

- ```add()```: Adds an element to the set
- ```clear()```: Removes all the elements from the set
- ```copy()```: Returns a copy of the set
- ```difference()```: Returns a set containing the difference between two or more sets
- ```intersection()```: Returns a set, that is the intersection of two other sets
- ```discard()```: Remove the specified item
- ```pop()```: Removes the element from the set
- ```remove()```: Removes the specified element
- ```union()```: Return a set containing the union of sets


In the next sections we are going to cover the above methods

#### Creating Sets

There are two aproches if we want to create sets:

1. Using ```{}```
2. Using ```set()```

Let's see some examples

```python
first_set = {1,2,3,4,5,1,2,3,4,5}
another_set = set([1,2,3,4,5,5,5,5,6])
```

#### Inserting elements

When we are dealing with sets we frequently need to add new elements, in order to do that we can use 
the method ```add()``` 

```python
numbers = {1,2,3,4}
numbers.add(5)
numbers.add(6)
numbers.add(4)
```

The result of the aboce code is going to be a set with the next values

```{1, 2, 3, 4, 5, 6}```

#### Set Union

We can combine the elements of two sets using the union operation.

```python
numbers_one = {1,2,3,4,5}
numbers_two = {4,5,6,7,8,9}
result = numbers_one.union(numbers_two)
```

The result is going to be

```{1, 2, 3, 4, 5, 6, 7, 8, 9}```

#### Set Intersection

The set interseccion are the common elements in both sets.

```python
numbers_one = {1,2,3,4,5}
numbers_two = {4,5,6,7,8,9}
result = numbers_one.union(numbers_two)
```

The result is:

```{4, 5}```

### Tuples

