# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем
# Об окончании ввода данных свидетельствует пустая строка

with open(r'data.txt', encoding='utf-8', mode='w') as my_file:
    while True:
        line = input('Введите текст построчно(завершить - пустая срока): ')
        if my_file.writable():
            my_file.writelines('\n' + line)
        if not line:
            break

my_file = open(r'data.txt', encoding='utf-8', mode='r')
print('\n\x1b[34mЧитаем записанные сроки в файл:\x1b[0m', f'{my_file.read()}')
my_file.close()
