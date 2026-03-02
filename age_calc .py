name = input("Як вас звати? ")
age = int(input("Скільки вам років? "))

ageinmonth = age * 12  # переводимо в місяці
ageinday = age * 365  # приблизно переводимо в дні

# вивід
print("Привіт")
print("Вас звати", name)
print("Вам", age, "років")
print("Або", ageinmonth, "місяців")
print("Вам", ageinday, "днів")