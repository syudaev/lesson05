# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран

def str_to_num(user_string):
    """Проверка ввода числа"""
    user_string = user_string.strip()
    if '.' in user_string and user_string.replace('.', '').isdigit():
        return float(user_string)
    elif user_string.isdigit():
        return int(user_string)


with open(r'my_numeric.txt', encoding='utf-8', mode='w') as my_file:
    line = input('Введите числа, разделенные пробелами: ')
    my_file.writable()
    my_file.writelines(line)

with open(r'my_numeric.txt', encoding='utf-8', mode='r') as my_file:
    str_list = my_file.read().split()

num_list = []
for i in str_list:
    if str_to_num(i) is not None:
        num_list.append(str_to_num(i))

print(f'\x1b[34m\nСумма чисел в файле >>>\x1b[0m {sum(num_list):>.2f}')
