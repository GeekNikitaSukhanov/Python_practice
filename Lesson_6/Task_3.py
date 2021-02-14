'''
Реализовать базовый класс Worker (работник).

●	определить атрибуты: name, surname, position (должность), income (доход);
●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus};
●	создать класс Position (должность) на базе класса Worker;
●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
 и дохода с учётом премии (get_total_income);
●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.
'''
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {wage: [wage], bonus: [bonus]}

class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(f'Полное имя сотрудника - {full_name}')
    def get_total_income(self):
        full_income = float(self.wage) * 12 + float(self.bonus)
        print(f'Полный доход сотрудника с учетом премии - {full_income}')


office_plankton = Position('Ivan', 'Kozlov', 'Analyst', 100, 50)
office_plankton.get_full_name()
office_plankton.get_total_income()





