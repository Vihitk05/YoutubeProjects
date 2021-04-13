"""

    # Tuples
    Tuple is another Data Structure which is almost similar to Lists.
    You can insert data of all primitive data types. But the only difference is
    that you cannot change elements in a tuple after creation like lists.
    So why Tuples? if we have Lists? The reason behind this is tuples are kind
    of secured. And because of which it has a very good feature in it called as Tuple
    Unpacking. By doing so, you can access each elements individually and without
    indexing into it. That's what makes a tuple different from a list.

"""
my_info = ('Vihit', 'Khetle', 17, 85.0)
other_info = ('John', 'Smith', 20, 90.0)

info_list = [my_info, other_info]

for first_name, last_name, age, percentage in info_list:
    print(first_name)
    print(last_name)
    print(age)
    print(percentage)
