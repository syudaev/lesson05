# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами
# и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

my_dict, profit_dict, aver_dict, loss_dict = {}, {}, {}, {}
profit_firm, profit_average, i = 0, 0, 0

with open('my_firm.txt', encoding='utf-8', mode='r') as my_file:
    for line in my_file:
        loss_firm = 0
        firma_name, firma_type, revenues, costs = line.split()
        my_dict[firma_name] = int(revenues) - int(costs)
        if my_dict.setdefault(firma_name) >= 0:
            profit_average = profit_average + my_dict.setdefault(firma_name)
            profit_dict[firma_name] = my_dict.setdefault(firma_name)
            i += 1
        else:
            loss_dict[firma_name] = my_dict.setdefault(firma_name)

    profit_average = profit_average / i
    aver_dict['profit_average'] = round(profit_average)
    my_list = [profit_dict, aver_dict, loss_dict]
    print(f'\n\x1b[34mСписок содержит словари: фирмы с прибылью, средняя прибыль, фирмы с убытками\n\x1b[0m{my_list}')

with open(r"my_file.json", encoding='utf-8', mode='w') as my_json:
    json.dump(my_list, my_json)
    json_string = json.dumps(my_list)
    print(f'\n\x1b[34mИтоговый список сохранен в виде json-объекта в файл my_file.json:\n\x1b[0m{json_string}')
