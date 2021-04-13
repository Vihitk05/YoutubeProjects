"""

    # Dictionaries
    Dictionaries are almost like a simple dictionary where in you have a "word" which
    in programming means a "key" and the "meaning of that word" which in programming
    means "value". In a normal dictionary, a word can have multiple meanings,likewise,
    in Dictionaries, a key can have multiple values in it. A normal dictionary can have
    different words but same meaning, similarly, different keys in dictionaries can
    have same values.

"""
my_dict = {
    1: ["Vihit", 17],
    2: ('john', 18),
    3: ['Jack']
}
# print(my_dict[1][0])
# print(my_dict.get(2))

user_input = int(input('Enter the number of whose you want to know the information: '))
print(my_dict[user_input][0])
