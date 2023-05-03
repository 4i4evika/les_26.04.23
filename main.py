### 1. Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список
# (тип списка нужно выбрать в зависимости от поставленной ниже задачи). После чего нужно показать меню,
# в котором предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю об этом,
# без добавления числа).
# 2. Удалить все вхождения числа из списка(пользователь вводит с клавиатуры число для удаления)
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала или с конца)
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все вхождения)
# В зависимости от выбора пользователя выполняется действие, после чего меню отображается снова.

# class Numbers:
#     def __init__(self):
#         self.lst = []
#
#     def push(self):
#         number1 = int(input('Введите число для добавления в список: '))
#         if number1 in self.lst:
#             print('Число не добавлено, т.к. уже существует такое число в списке')
#         else:
#             self.lst.append(number1)
#         print(self.lst)
#
#     def pop(self):
#         number2 = int(input('Введите число для удаления из списка: '))
#         if len(self.lst) == 0:
#             print('Список пустой')
#         elif number2 in self.lst:
#             self.lst.remove(number2)
#         else:
#             print('Такого числа нет в списке')
#         print(self.lst)
#
#     def show(self):
#         answer = int(input('Введите 1 для вывода списка с начала, 2 для вывода списка с конца: '))
#         if answer == 1:
#             print(self.lst)
#         elif answer == 2:
#             print(self.lst[::-1])
#         else:
#             print('Введено неверное значение')
#
#     def check(self):
#         number3 = int(input('Введите число, которое нужно найти: '))
#         if number3 in self.lst:
#             print(f'Число {number3} есть в списке')
#         else:
#             print(f'Числа {number3} нет в списке')
#         print(self.lst)
#
#     def edit(self):
#         number4 = int(input('Введите число, которое нужно заменить: '))
#         number5 = int(input('Введите новое значение: '))
#         if number4 in self.lst:
#             for i in range(len(self.lst)):
#                 if self.lst[i] == number4:
#                     self.lst[i] = number5
#         else:
#             print(f'Числа {number4} нет в списке')
#         print(self.lst)
#
#
# number = Numbers()
#
# while True:
#     menu = ('Добавить новое число', 'Удалить число', 'Показать содержимое списка', 'Проверить наличие числа в списке',
#             'Заменить значение в списке')
#     count = 0
#     print('-------------------------------------------------------------------------------')
#     for i in menu:
#         count += 1
#         print(count, " - ", i)
#     print()
#
#     x = int(input('Выберите действие, которое вы хотите выполнить: '))
#     if x == 1:
#         number.push()
#     elif x == 2:
#         number.pop()
#     elif x == 3:
#         number.show()
#     elif x == 4:
#         number.check()
#     elif x == 5:
#         number.edit()
#     else:
#         break


### 2. Реализуйте класс стека для работы со строками (стек строк). Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки из стека.
# При старте приложения нужно отобразить меню с помощью, которого пользователь может выбрать необходимую операцию.

# class Stack:
#     def __init__(self, size):
#         self.lst = []
#         self.size = size
#
#     def push(self, value):
#         if self.full():
#             print('Стек полный')
#         elif not isinstance(value, str):
#             print(f'Аргумент {value} неверного типа данных')
#         else:
#             self.lst.append(value)
#
#     def full(self):
#         return len(self.lst) == self.size
#
#     def empty(self):
#         if len(self.lst) == 0:
#             return 'Стек пустой'
#         return False
#
#     def pop(self):
#         return self.empty() or self.lst.pop()
#
#     def peek(self):
#         return self.empty() or self.lst[-1]
#
#     def clear(self):
#         self.lst.clear()
#         print('Стек очищен')
#
#     def length(self):
#         return len(self.lst)
#
#     def __str__(self):
#         return ' -> '.join(map(str, self.lst))
#
#
# stack = Stack(4)
# stack.push('ggg')
# stack.push('hhh')
# stack.push(5)
# stack.push('jjj')
# stack.push('lll')
# print(stack)
# print(stack.pop())
# print(stack.peek())
# print(stack.empty())
# print(stack.full())
# print(stack.length())



### 3. Измените стек из второго задания, таким образом, чтобы его размер был нефиксированным.

# class Stack:
#     def __init__(self):
#         self.lst = []
#
#     def push(self, value):
#         if not isinstance(value, str):
#             print(f'Аргумент {value} неверного типа данных')
#         else:
#             self.lst.append(value)
#
#     def empty(self):
#         if len(self.lst) == 0:
#             return 'Стек пустой'
#         return False
#
#     def pop(self):
#         return self.empty() or self.lst.pop()
#
#     def peek(self):
#         return self.empty() or self.lst[-1]
#
#     def clear(self):
#         self.lst.clear()
#         print('Стек очищен')
#
#     def length(self):
#         return len(self.lst)
#
#     def __str__(self):
#         return ' -> '.join(map(str, self.lst))
#
#
# stack = Stack()
# stack.push('ggg')
# stack.push(5)
# stack.push('kkk')
# stack.push('jjj')
# stack.push('lll')
# print(stack)
# print(stack.pop())
# print(stack.peek())
# print(stack.empty())
# print(stack.length())