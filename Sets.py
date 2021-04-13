"""

    # Sets
    Set is also a Data Structure where you can add elements of all primitive
    data types. Its almost similar to Lists & Tuples. The only difference is that
    it doesn't allow duplicate elements in it where as in Lists & Tuples Duplicate
    elements are allowed. Sets basically comes from the mathematical term Sets where in
    you have venn diagram. It has all the attributes or functions of that mathematical
    set. i.e. it has union, intersection etc.

"""
banana = {'Yellow', 'smooth', 'sweet'}
lemon = {'Yellow', 'sour', 'bumpy'}

# print(banana.union(lemon))
# print(banana.intersection(lemon))

# Conversion of tuple into set
my_tuple = (1, 1, 2, 2, 3, 3)
my_tuple1 = set(my_tuple)
# print(my_tuple1)

# Conversion of list into set
my_list = [1, 1, 2, 2, 3, 3]
# my_list1 = set(my_list)
print(set(my_list))
