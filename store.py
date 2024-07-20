'''
Описати мережу магазинів за допомогою наших класів:

Додати можливість додавати до нашого магазину продукти

Додати можливість до нашого магазину додавати працівників


class Store:
    address: str
    name: str
    products: list[Product]
    employees: list[Employee]

class Product:
    quantity: int
    price: float

class Milk(Product):
    type: str

class Bread(Product):
    type: str

class Employee:
    first_name: str
    last_name: str

class Cashier(Employee):
    cash_desk_number: int

class Security(Employee):
    access_level: int

'''
from employee import Employee, Security, Cashier


class Store:
    def __init__(self) -> None:
        self.employees = dict()
        self.products = []

    def add_employee(self, employee: Employee):
        id = employee.id
        self.employees[id] = employee

    def return_employee_names(self) -> list[str]:
        employee_names = []
        for id, employee in self.employees.items():
            employee_name = f'{employee.first_name} {employee.last_name}'
            employee.first_name = 'Employee'
            employee_names.append(employee_name)
        return employee_names

cashier = Cashier('John', 'Doe', 1)
security_one = Security('Alice', 'Doe', 2)
security_two = Security('Bella', 'Doe', 2)
store_one = Store()
store_one.add_employee(cashier)
store_one.add_employee(security_one)
store_one.add_employee(security_two)

# print(store_one.employees)

# print(store_one.employees[1].first_name)
print(store_one.return_employee_names())
print(store_one.return_employee_names())
