def create_account(*args, **kwargs):
    save_to_database(kwargs)
    return {
        'username': args[0],
        'password': password,
        'age': kwargs['age'],
        'avatar': avatar,
        'address1': address1,
        'address2': address2,
        'phone': phone,
        'email': email,
        'cc': cc,
    }


# new_user = create_account(username='jeffwinner', email='hello@world.com', password='snanoetuoaeidg',
#                           age=None, avatar='', address1='', address2='', phone='', cc=None)
# print(new_user)te_account(username='jeffwinner', email='hello@world.com', password='snanoetuoaeidg',
#                           age=None, avatar='', address1='', address2='', phone='', cc=None)
# print(new_user)


def add_to_cart(*args):
    pass


def addme(num1, num2, *args):
    print(num1, num2, args)
    total = num1 + num2
    # limit = 0
    for i in args:
        total += i
    return total


print(addme(10, 3))


def profile_generator(*args, **kwargs):
    print(args, kwargs)


profile_generator(123, 456, 11, 'eoueoueo', username='jeff', password='abc123', age=123)
