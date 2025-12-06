Задание 1
#
# try:
#     userInfo = input("Введите ваше имя и возраст через пробел: ")
#     words = userInfo.split()
#     if len(words) != 2:
#         raise ValueError("Нужно ввести имя и возраст через пробел")
#     name = words[0]
#     age = int(words[1])
#     if age < 0 or age > 130:
#         print("Ошибка: введен некорректный возраст")
#     else:
#         print(f"Привет, {name}! Твой возраст — {age}")
# except ValueError as ex:
#     print(f"Ошибка ввода: {ex}")
# finally:
#     print("Успешное знакомство")
#
# Задание 2(1)
#
# def userinfo(nameage):
#     words = nameage.split()
#     if len(words) != 2:
#         raise ValueError("Нужно ввести имя и возраст через пробел")
#     name = words[0]
#     age = int(words[1])
#     if age < 0 or age > 130:
#         print("Ошибка: введен некорректный возраст")
#     else:
#         print(f"Привет, {name}! Твой возраст — {age}")
#
# try:
#     userinfo("Роман 26")
# except ValueError as ex:
#     print(f"Ошибка ввода: {ex}")
# finally:
#     print("Успешное знакомство")
#
# Задание 2(2)
#
# def userinfo(nameage):
#     try:
#         words = nameage.split()
#         if len(words) != 2:
#             raise ValueError("Нужно ввести имя и возраст через пробел")
#         name = words[0]
#         age = int(words[1])
#         if age < 0 or age > 130:
#             print("Ошибка: введен некорректный возраст")
#         else:
#             print(f"Привет, {name}! Твой возраст — {age}")
#     except ValueError as ex:
#         print(f"Ошибка ввода: {ex}")
#     finally:
#         print("Успешное знакомство")
#
# userinfo("Роман 26")
#
# Задание 3
#
# try:
#     numbers = input("Введите набор случайных позитивных чисел через запятую\n\t: ")
#     inputnumbers = numbers.split(",")
#     for number in inputnumbers:
#         value = int(number)
#         if value < 0:
#             raise Exception("Число должно быть позитивным!")
#     total = 0
#     for number in inputnumbers:
#         total += int(number)
#     print("Сумма чисел:", total)
# except ValueError:
#     print("Ошибка: нужно вводить только числа!")
# except Exception as ex:
#     print("Ошибка:", ex)
# finally:
#     print("Обработка завершена")
#
# Задание 4(1)
#
# def numbers(numberslist):
#     total = 0
#     for number in numberslist:
#         if number < 0:
#             raise Exception("Число должно быть позитивным!")
#         total += number
#     return total
#
# try:
#     result = numbers([5, 10, 3, 7])
#     print("Сумма чисел:", result)
# except Exception as ex:
#     print("Ошибка:", ex)
# finally:
#     print("Обработка завершена")
#
#
# Задание 4(2)
#
# def numbers(numberslist):
#     try:
#         total = 0
#         for number in numberslist:
#             if number < 0:
#                 raise Exception("Число должно быть позитивным!")
#             total += number
#         print("Сумма чисел:", total)
#     except Exception as ex:
#         print("Ошибка:", ex)
#     finally:
#         print("Обработка завершена")
#
# numbers([5, 10, 3, 7])
#
# Задание 5
#
# numbers = []
#
# while True:
#     userNum = input("Введите число для наполнения списка,\n или слово стоп для перехода в меню: ")
#     if userNum.lower() == 'стоп':
#         break
#     try:
#         numbers.append(float(userNum))
#     except ValueError:
#         print("Ошибка: введите число!")
# while True:
#     print("Введите цифру нужного действия:"
#           "\n\t1.Показать\n\t 2.Макс\n\t 3.Мин\n\t 4.Элемент\n\t 5.Удалить\n\t 6.Выход")
#     choice = input("Выберите действие: ")
#     try:
#         if choice == '1':
#             print(numbers)
#         elif choice == '2':
#             print(max(numbers))
#         elif choice == '3':
#             print(min(numbers))
#         elif choice == '4':
#             index = int(input("Индекс: "))
#             print(numbers[index])
#         elif choice == '5':
#             index = int(input("Индекс для удаления: "))
#             print("Удалено:", numbers.pop(index))
#         elif choice == '6':
#             break
#         else:
#             print("Неверный пункт")
#     except (ValueError, IndexError):
#         print("Ошибка: неверный ввод или индекс")