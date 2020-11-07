# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран

result_sum = 0

with open(r'my_numeric.txt', encoding='utf-8', mode='w') as my_file:
    line = input('Введите числа, разделенные пробелами: ')
    my_file.writable()
    my_file.writelines(line)

with open(r'my_numeric.txt', encoding='utf-8', mode='r') as my_file:
    str_list = my_file.read().split()
    for i in range(len(str_list)):
        if str_list[i].isdigit():
            result_sum = result_sum + int(str_list[i])
        elif not str_list[i].isdigit():
            try:
                result_sum = result_sum + float(str_list[i])
            except ValueError:
                print(f'{str_list[i]:>5}', '>>>', "\x1b[31m", 'Ошибка! Вводите только числа!', "\x1b[0m")
                continue
    print(f'\x1b[34m\nСумма чисел в файле >>>\x1b[0m {result_sum:>.2f}')
