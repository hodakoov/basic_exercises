print('#####Задача №1#####')
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

repit = {}
for student in students:
    name = student['first_name']
    if name in repit:
        repit[name] += 1
    else:
        repit[name] = 1

for k, v in repit.items():
    print(f'{k}: {v}')

print('#####Задача №2#####')
# Задание 2
# Дан список учеников, нужно вывести самое часто повторяющееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

repit = {}
for student in students:
    name = student['first_name']
    if name in repit:
        repit[name] += 1
    else:
        repit[name] = 1
result = ''
max = 0
for k, v in repit.items():
    if v > max:
        max = v
        result = k
print(f'Самое частое имя среди учеников: {result}')

print('#####Задача №3#####')
# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
repit = {}
class_num = 0
for class_school in school_students:
    class_num += 1
    for student in class_school:
        name = student['first_name']
        if name in repit:
            repit[name] += 1
        else:
            repit[name] = 1
    result = ''
    max = 0
    for k, v in repit.items():
        if v > max:
            max = v
            result = k
    repit = {}
    print(f'Самое частое имя в классе {class_num}: {result}')

print('#####Задача №4#####')
# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
male = 0
for class_school in school:
    class_number = class_school['class']
    for student in class_school['students']:
        if is_male[student['first_name']]:
            male += 1
    print(f'Класс {class_number}: девочки {len(class_school["students"]) - male}, мальчики {male}')
    male = 0
print('#####Задача №5#####')
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

male = 0
woman = 0
for class_school in school:
    class_number = class_school['class']
    for student in class_school['students']:
        if is_male[student['first_name']]:
            male += 1
        else:
            woman += 1
        if male > woman:
            result = 'мальчиков'
        else:
            result = 'девочек'
    print(f'Больше всего {result} в классе {class_number}')
    male = 0
    woman = 0
