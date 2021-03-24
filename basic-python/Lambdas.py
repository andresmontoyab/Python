#Lambdas Functions functions as

print("First Lambda Function")
lambda_sum = lambda a: a+1
print("The Sum of ", lambda_sum(100))
print("------------------")

print("Map Lambda Function")
def letter_to_lenght(str):
    return len(str)
lengths = map(letter_to_lenght, ("Java", "React"))
print(list(lengths))
print("------------------")


print("Filter Lambda Functions")
def greater_than_5(num):
    if num>5: return num
num_greater_than_5 = filter(greater_than_5,(1,2,3,4,5,6,7,8,9))
print(list(num_greater_than_5))
print("------------------")

print("Reduce Lambda Functions")
def sum(a,b):
    return a+b

from functools import reduce
print(reduce(sum, [1,2,3,4,5,6,]))
print("------------------")