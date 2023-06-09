class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'''"{self.name} {self.surname}, {self.city}, Баланс: {self.balance}".'''

    def get_guest(self):
        return f'{self.name} {self.surname}, г. {self.city}'

client_1 = Clients('Иван', 'Петров', 'Москва', 50)
client_2 = Clients('Владимир', 'Зайцев', 'Кострома', 50)
client_3 = Clients('Олеся', 'Янина', 'Новосибирск', 50)

guest_list = [client_1, client_2, client_3]

for guest in guest_list:
    print(guest.get_guest())
