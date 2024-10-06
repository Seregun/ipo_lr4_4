def list(input_list): # Определение функции list, которая принимает список input_list
    tripled_list = [string * 3 for string in input_list] # Создание нового списка (строки умноженные на 3)
    return tripled_list # возвращение полученного списка
input_list = input("Введите список строк через запятую: ").split(", ") # Ввод списка строк через запятую
tripled_list = list(input_list) # Вызов функции list, сохраняя результат в tripled_list
print("Новый список строк, где каждая строка записана трижды:", tripled_list) # Вывод полученного списка строк