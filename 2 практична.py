hello = "Hello World"
name = "Pavlo"
last_name = "Bezushkevich"
age = 16

# Створюємо список з типами змінних
types_list = [type(hello), type(name), type(last_name), type(age)]

# Виводимо типи на екран
print("Типи змінних:", types_list)

# Перевіряємо, чи всі типи однакові
if len(set(types_list)) == 1:
    print("good")
else:
    # Видаляємо тип даних, який відрізняється
    unique_types = list(set(types_list))
    for t in unique_types:
        if types_list.count(t) == 1:
            types_list.remove(t)
    print("Виправлений список типів:", types_list)





