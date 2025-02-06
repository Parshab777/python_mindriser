#  Indexing and Slicing - can only be done in Sequential Datatype.


# a = "Hello World"

# # print(a[0:4])

# # [start: end(This is not included else it can be taken as -1): jump]

# print(a[1::2])



# a = "Ram is ( programmer"

# print(a[7:8])
# print(a[9:])


# List


# a= ['apple','banana','litchi']


# print(a[1])


# a[1] = "Mango"     # It is mutable so we can change its element.

# print(a)




# Tuple:

# a= ('apple','banana','litchi')

# print(a[0:1])


# # a[1] = "Mango"     # It is im-mutable so we cannot change its element.


# # To do: remove duplicate data

# a = ('apple', 'grape', 'mango', 'orange','watermelon','mango','orange','watermelon')


# b = set(a)

# print(b)


# # Dictionary - In this we have to print the key.

# person = { 'name' : 'parshab',
#             'age': '25',
#             'hobbies': ['reading books' , 'sleeping','drawing']
# }

# print(person['name'])

# print(person['age'])


# To print hobbies data at 1 index.
# print(person['hobbies'][1])

# To print only the term "book". 
# print(person['hobbies'][0][8:])



# TO change the elements of the dictionary.

# person = { 'name' : 'parshab',
#             'age': '25',
#             'hobbies': ['reading books' , 'sleeping','drawing']}

# person["name"] = "diya"

# print(person)


# To do: 
a = ('apple', 'mango', 'orange', 'grape', 'watermelon')

b = list(a)

b[0]="grapes"


c= tuple(b)


print(c)
