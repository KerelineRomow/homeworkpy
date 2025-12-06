# # Завдання 1
#
# capitals = {"Україна": "Київ", "Польща": "Варшава", "Німеччина": "Берлін"}
# for country in capitals.keys():
#     print(f"Країна: {country}")
# for city in capitals.values():
#     print(f"Місто: {city}")
# print("________________")
# coCyDict = dict(capitals)
# coCyDict.update({"Франція": "Париж"})
# for country in coCyDict.keys():
#     print(f"Країна: {country}")
# for city in coCyDict.values():
#     print(f"Місто: {city}")
#
# # Завдання 2
#
# prices = {"яблуко": 15, "банан": 20, "груша": 18}
# buyerUnit = input("Введіть назву товару: ")
# if buyerUnit in prices:
#     print(f"Ціна товару {buyerUnit} : {prices[buyerUnit]} грн")
# elif buyerUnit.isdigit():
#     print("Помилка! Вводьте назву товару літерами.")
# else:
#     print("Такого товару немає в магазині.")

# Завдання 3

# firm = {
#     "Іванов Іван Іванович":
#         {"телефон": "+38067...", "email": "ivanov@company.ua",
#          "посада": "Менеджер", "кабінет": 101, "skype": "ivanov_live"},
#     "Петренко Ольга Сергіївна":
#         {"телефон": "+38099...", "email": "petrenko@company.ua",
#          "посада": "Програміст", "кабінет": 205, "skype": "olga.petrenko"},
#     "Ковальчук Марія Василівна":
#         {"телефон": "+38063...", "email": "kovalchuk@company.ua",
#          "посада": "Бухгалтер", "кабінет": 108, "skype": "maria_koval"}
# }
#
# while True:
#     menu = input("Введіть цифру потрібної функції\n\t"
#                  "1)Показати працівників\n\t"
#                  "2)Додати працівника\n\t"
#                  "3)Знайти працівника\n\t"
#                  "4)Змінити дані працівника\n\t"
#                  "5)Видалити дані працівника\n\t"
#                  "6)Вихід\n")
#
#     if menu == "1":
#         for fullN, info in firm.items(): print(fullN, info)
#     elif menu == "2":
#         name = input("ПІБ: ")
#         if name not in firm:
#             firm[name] = {"телефон": input("тел: "), "email": input("email: "), "посада": input("посада: "),
#                           "кабінет": input("каб: "), "skype": input("skype: ")}
#             print("Додано")
#     elif menu == "3":
#         person = input("ПІБ: ")
#         print(firm.get(person, "Немає такого працівника"))
#     elif menu == "4":
#         person = input("ПІБ: ")
#         if person in firm:
#             find = input("Введіть пункт, який потрібно змінити: ")
#             if find in firm[person]:
#                 firm[person][find] = input("Нове значення: ")
#                 print("Змінено")
#             else:
#                 print("Помилкове введення!")
#     elif menu == "5":
#         name = input("ПІБ для видалення: ")
#         deleted = firm.pop(name, None)
#         if deleted is None:
#             print("Помилкове введення!")
#         else:
#             print("Видалено")
#     elif menu == "6":
#         break

# Завдання 4

# def gluedicts(dict1, dict2):
#     result = {}
#     for key, value in dict1.items():
#         result[key] = value
#     for key, value in dict2.items():
#         if key in result:
#             result[key] += value
#         else:
#             result[key] = value
#
#     return result
#
# a = {"x": 10, "y": 5, "z": 3}
# b = {"y": 7, "z": 1, "w": 4}
#
# print(gluedicts(a, b))

# Завдання 5:

# text = input("Введіть текст: ")
#
# words = text.split()
# result = {}
#
# for word in words:
#     if word in result:
#         result[word] += 1
#     else:
#         result[word] = 1
#
# print(result)