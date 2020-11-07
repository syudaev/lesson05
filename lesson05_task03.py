# Часть1 -Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников
# Выполнить подсчет средней величины дохода сотрудников
# Пример файла:(Иванов 23543.12 Петров 13749.32)
# ---------------------------------------------------------------------------------------------------------------
# Часть2 - Создать (не программно) текстовый файл со следующим содержимым: # (One — 1 Two — 2 Three — 3  Four — 4)
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные, при этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл

import time

with open(r'my_salary.txt', encoding='utf-8', mode='r') as my_file:
    my_list = my_file.read().split('\n')
    user_salary, low_salary, total_salary = [], [], []
    # low_salary = []
    for i in my_list:
        i = i.split()
        try:
            total_salary.append(i[1])
            if float(i[1]) < 20000:
                low_salary.append(i[0])
            else:
                user_salary.append(i[1])
        except IndexError:
            print('\n\x1b[31mНе корректный формат исходного файла!\x1b[0m')

print('\n\x1b[34mСотрудники с окладом менее 20 тыс:\x1b[0m', '\n'.join(low_salary), sep='\n')
print('\x1b[34mСредний оклад >>>\x1b[0m', f'{sum(map(float, total_salary)) / len(total_salary):.2f}')

print('\n\x1b[34mЧерез 3 секунды запустится второй блок задания\x1b[0m')
time.sleep(3)

rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_numbers = []
with open(r'my_numbers.txt', encoding='utf-8', mode='r') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        rus_numbers.append(rus_dict[i[0]] + ' ' + i[1].replace('\n', ''))

with open('my_numbers_rus.txt', encoding='utf-8', mode='w') as my_file_rus:
    my_file_rus.writelines('\n'.join(rus_numbers))

with open('my_numbers_rus.txt', encoding='utf-8', mode='r') as my_file_rus:
    print('\n\x1b[34mEng числительные заменены на Rus, блок записан в новый текстовый файл:\x1b[0m',
          my_file_rus.read(), sep='\n')
