from subprocess import list2cmdline

countries = ['United Kingdom', 'Nepal', 'India', 'China']
print(countries[2][0])
print(countries[2])
print(countries[1:])
print(countries[1:3])
print(type(countries))
name = 12
print(type(name))
countries[0] = 'United States'
print(countries[-2])
print(len(countries))
print(type(countries[1]))
hello = list(('Nepal',34,False))
print(hello)

#List Methods
list1 = [4, 3, 5, 1, 2,]
list2 = ['banana', 'apples', 'mango', 'oranges', 'mango']
list2.append('cherry')
print(len(list2))
print(list2)
list2.insert(1, 'graphes')
print(list2)
print(list2.index('mango'))
print(list2.count('mango'))
list1.sort()
print(list1)
list2.reverse()
print(list2)
list3 =list2.copy()
print(list3)
list2.pop()
print(list2)
list2.pop(1)
print(list2)
list2.remove('banana')
print(list2)
del list2[0]
print(list2)
del list2
print(list1)