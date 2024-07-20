'''
Написати функцію, яка буде повертати унікальний ідентифікатор
'''
1, 2, 3, 4 

id = 0

def get_unique_identifier():
    global id
    id += 1
    return id

# print(get_unique_identifier())
# print(get_unique_identifier())
# print(get_unique_identifier())
# print(get_unique_identifier())

def get_unique_identifier_closure():
    id = 0
    def get_next_value():
        nonlocal id
        id += 1
        return id
    return get_next_value

id_generator = get_unique_identifier_closure()
# print(id_generator())
# print(id_generator())
# print(id_generator())
# print(id_generator())

# fn(3)(5)(6) -> 14
#

def fn(a: int):
    def fn_2(b: int):
        def fn_3(c: int):
            # nonlocal a
            # nonlocal b
            return a + b + c
        return fn_3
    return fn_2

# print(fn(3)(5)(6))

# fn('John')('Doe')('1234567890') -> 'Person name is John Doe and his phone number is 1234567890'
def get_user_info(first_name: str):
    def get_user_last_name(last_name: str):
        def get_user_phone_number(phone_number: str):
            nonlocal first_name
            first_name = f'{first_name[0]}.' # 'J.'
            return f'Person name is {first_name} {last_name} and his phone number is {phone_number}'
        return get_user_phone_number
    return get_user_last_name

# print(get_user_info('John')('Doe')('1234567890'))


