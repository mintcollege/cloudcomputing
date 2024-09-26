from icecream import ic

age = 18            # int
name: str = 'John Doe'   # str
height = 5.5        # float
height = int(height)
groupmates = ['Monty', 'Python', 'Jane Doe']       # list
uneditable_groupmates = ('Monty', 'Python', 'Jane Doe')        # tuple
short_tuple = ('Michael',)      # tuple
numbers = {1, 2, 3, 2, 5, 3}        # set
# no_duplicates_list = list(set(numbers))
user_info = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 18,
}       # dict
paid = True     # bool
all_users = [
    {
        'id': 134534656,
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 18,
    }
]
ic(numbers)