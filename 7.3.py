'''
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух
клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
'''

class Cell:
    def __init__(self, count_cell):
        self.count_cell = int(count_cell)

    def __add__(self, other):
        return f'Объединение двух клеток (сложение): {self.count_cell + other.count_cell}'

    def __sub__(self, other):
        if self.count_cell - other.count_cell > 0:
            return f'Участвуют две клетки (вычитание): {self.count_cell - other.count_cell}'
        else:
            return f'Вычитаниедвух клеток невозможно, так как разность отрицательная: {self.count_cell - other.count_cell}'

    def __mul__(self, other):
        return f'Создается общая клетка из двух (умножение): {self.count_cell * other.count_cell}'

    def __floordiv__(self, other):
        if other.count_cell == 0:
            return 'Нет смысла, если вторая клетка отсутствует'
        else:
            return f'Создается общая клетка из двух (деление): {self.count_cell // other.count_cell}'

    def make_order(self, num):
        my_str = ''
        for i in range(int(self.count_cell / num)):
            my_str += f'{"*" * num} \\n'
        my_str += f'{"*" * (self.count_cell % num)}'
        return my_str


a = Cell(input('Введите количество ячеек: '))
b = Cell(input('Введите количество ячеек: '))
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a.make_order(5))
print(b.make_order(5))