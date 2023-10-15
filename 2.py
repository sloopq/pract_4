def obsh(number1, number2):
    peresech = set(number1) & set(number2)
    return len(peresech)


number1 = input("Введите первый список ").split()
number2 = input("Введите второй список ").split()

result = obsh(number1, number2)
print("Количество общих чисел: ", result)

