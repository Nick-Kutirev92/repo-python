number = int(input('Введите число от 1 до 20: '))

while number >= 0 and number <= 20:
    if number >= 2 and number <= 4:
        print(number, 'процента')
    elif number == 0 or number >= 5 and number <= 20:
        print(number, 'процентов')
    else:
        print(number, 'процент')
    break
#