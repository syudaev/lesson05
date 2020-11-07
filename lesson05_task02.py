# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке

with open(r'my_data.txt', encoding='utf-8', mode='a') as my_file:
    while True:
        line = input('Введите текст построчно(завершить - пустая срока): ')
        if my_file.writable():
            my_file.writelines('\n' + line)
        if not line:
            break

with open(r'my_data.txt', encoding='utf-8', mode='r') as my_file:
    print('\n\x1b[34mЧитаем готовый файл и записанные в него строки:\x1b[0m', f'{my_file.read()}', sep='\n')
    my_file.seek(0, 0)
    number_string = my_file.readlines()
    print(f'\n\x1b[34mКоличество строк в файле -\x1b[0m {len(number_string)}')
    my_file.seek(0, 0)
    for i in range(len(number_string)):
        word_string = my_file.readline()
        print(f'{"Слов в строке "} {(i + 1):>2} {" >>> "} {len(word_string.split()):>2}',
              '(', word_string.replace('\n', ''), ')')
