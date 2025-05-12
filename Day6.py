#tuples

cities=("Mumbai","Jaunpur","Ghaziabad","Nagpur","Nashik")
print(cities[2])
print(cities[-1])
# cities[0]="Kanpur"
print(cities.count("Jaunpur"))

#----------------------------------------------------------------------------------------------------------------

#sets

numbers={12,34,32,111,222}
numbers.add(4444)
print(numbers)
numbers.add(4444)
print(numbers)
numbers.remove(4444)
print(numbers)

set1={12,34,56,43,34,23,234,222}
set2={12,56,23,3455,3333,21,121,12222,11}
unions=set1.union(set2)
print(unions)
intersections=set1.intersection(set2)
print(intersections)
differences=set1.difference(set2)
print(differences)
