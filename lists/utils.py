# copy, count, sort, reverse, index methods

x = [12,231,45,56,12,45,21,1,1,1,1]
y = x.copy() # creates a copy of x
print(x)
print(y)

c1 = x.count(1) # count the number of occurences of 1 in x
print(f'1 occurs {c1} times in x')

x.sort() # sorts x in ascending order
print(x)
x.sort(reverse=True) # sorts x in descending order
print(x)
y.reverse() # reverses the order of y same as y[::-1]
print(y)

i231 = y.index(231) # returns the index of value 231 in y
print(f'231 is at index {i231} in y')
i12 = y.index(12) # returns the index of first occurence of 12 in y
print(f'12 is at index {i12} in y')