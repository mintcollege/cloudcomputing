from icecream import ic


# user_info = {
#     'id': 134534656,
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 18,
# }
# ic(user_info)

def calculate(num1: int, num2: int = 10, num3: int = 0) -> int:
    """
    Calculates the sum of 3 numbers and return an integer.
    """
    return num1 + num2 + num3
    # return 'hello'
    # return True
    # return None


def login(username: str, password: str) -> bool:
    """
    Check the database if account exists.
    """
    successful = True
    return successful


def dothislater():
    pass


calculate(1, 2, 3)