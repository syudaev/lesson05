# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# аличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# ... т. д
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_dict, new_dict = {}, {}

with open('my_student.txt', encoding='utf-8', mode='r') as my_student:
    for line in my_student:
        subject, lecture, practical, laboratory = line.split()
        my_dict[subject] = lecture + practical + laboratory

    for key, value in my_dict.items():
        my_string = ''
        key = key.replace(':', '')
        for n in value:
            if n.isdigit():
                my_string = my_string + ''.join(n)
            else:
                my_string = my_string + n.replace(n, ' ')
            my_result = 0
            for i in my_string.split():
                my_result = my_result + int(i)
        new_dict[key] = int(my_result)

print(f'\n\x1b[34mОбщее количество занятий по предметам:\n\x1b[0m{new_dict}')
