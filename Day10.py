from functools import reduce

# def square(num):
#     return num*num
# print(square(5))

#----------------------------------------------------------------------------

# square=lambda x : x*x
# print(square(7))

#----------------------------------------------------------------------------

# nums=[2,4,6,8,9]
# square=list(map(lambda x : x**2, nums))  #💡 Use when you want to apply a function to every item in a list.
# print(square)

#----------------------------------------------------------------------------

# nums=[2,4,6,8,9,34,67,434,232,23233,23]
# filtered=list(filter(lambda x : x%2==0, nums))    #💡 Use when you want to filter out some items based on a condition.
# print(filtered)

#----------------------------------------------------------------------------

nums=[2,4,6,8,9,34,67,434,232,23233,23]
total =reduce(lambda x,y : x+y,nums)    #Use when you want to reduce a list to a single value (like sum, product, etc.)
print(total)
