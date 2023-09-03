if __name__ == "__main__":
    print("Zdorov")

    #Завдання 1:
    #Напишіть програму, яка запитує два цілих числа x і y, після чого обчислює і виводить значення x у степені y.

    #Розв'язок завдання:
    # x = int(input("Введіть число:"))
    # y = int(input("Введіть ступінь числа:"))
    #
    # potenza_di_numero = 1
    # for _ in range(y):
    #     potenza_di_numero *= x
    # print(potenza_di_numero)

    #Завдання 2
    #Підрахувати кількість цілих чисел у діапазоні від 100 до 999, у яких є дві однакові цифри.

    #Розв'язок задачі:
    # new_list = []
    # for item in range(100,1000):
    #     cifre = str(item)
    #     if len(set(cifre)) == 2:
    #         new_list.append(item)
    # print(len(new_list))

    #Завдання 3
    #Підрахувати кількість цілих чисел у діапазоні від 100 до 9999, у яких усі цифри різні.

    #Розв'язок задачі:
    # new_list = []
    # for item in range(100,1000):
    #     cifre = str(item)
    #     if len(set(cifre)) == len(cifre):
    #         new_list.append(item)
    # print(len(new_list))

    #Завдання 4
    #Користувач вводить будь-яке ціле число.
    #Необхідно з цього цілого числа видалити всі цифри 3 і 6 і вивести назад на екран.

    #Розв'язок завдання:
    # user_number = input("Введіть число:")
    # new_list = []
    # for item in user_number:
    #         new_list.append(int(item))
    # number_for_elimenate = [3,6]
    #
    # new_list = [x for x in new_list if x not in number_for_elimenate]
    # print(new_list)



