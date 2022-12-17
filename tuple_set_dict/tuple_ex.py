x = (1,2,3) # tuple
y = 2,5,2,1 # tuple packing
print(x)
print(y)
print(type(x))
print(type(y))
print(x[0]) # index 0
print(x[1]) # index 1
print(y[-1]) # index -1
z = (1,2,3,4,5,6,7,8,9,10)
print(z[:5]) # slicing

# tuple methods - count, index
a = ('Apple','Apple','Apple','Banana','Pine Apple','Custard Apple')
print(f'len of a is {len(a)}')
print(f'Apple occurs {a.count("Apple")} times')
print(f'Pine Apple occurs {a.count("Pine Apple")} times')
print(f'Banada is at index {a.index("Banana")}')

# tuple to list
zl = list(z)
print(type(z), type(zl))
print(z, zl)
# list to tuple
zt = tuple(zl)
print(type(zl), type(zt))
print(zl, zt)

# single item tuple 
s = (1,) # comma is important
s2 = 2, # is also a tuple
print(type(s))