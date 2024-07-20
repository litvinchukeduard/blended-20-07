from closure_example import get_unique_identifier_closure

id_generator = get_unique_identifier_closure()

class Employee:
    # def __init__(self) -> None:
    #     self.first_name = None
    #     self.last_name = None
    def __init__(self, first_name: str, last_name: str) -> None:
        # if len(first_name) < 1
        self.id = id_generator()
        self.first_name = first_name
        self.last_name = last_name


class Cashier(Employee):

    def __init__(self, first_name: str, last_name: str, cash_desk_number: int) -> None:
        super().__init__(first_name, last_name)
        self.cash_desk_number = cash_desk_number


class Security(Employee):
    def __init__(self, first_name: str, last_name: str, access_level: int) -> None:
        super().__init__(first_name, last_name)
        self.access_level = access_level


if __name__ == '__main__':
    cashier = Cashier('John', 'Doe', 1)
    security_one = Security('Alice', 'Doe', 2)
    security_two = Security('Bella', 'Doe', 2)

    employee_list = [Cashier('John', 'Doe', 1), Security('Alice', 'Doe', 2), Security('Bella', 'Doe', 2)]
    # employee_list = [cashier, security_one, security_two]
    for employee in employee_list:
        print(f'{employee.first_name} {employee.last_name}')
        # print(employee.access_level)
